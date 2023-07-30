'''
    Creates a chatbot
'''
import openai
from flask import jsonify
from dotenv import load_dotenv
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores.pgvector import PGVector
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain import PromptTemplate
from db_config import CONNECTION_STRING
load_dotenv()


def generate_response(user_ask):
    ''' Generate a response for a request '''

    # Extract text from PDF
    loader = PyMuPDFLoader("/home/bitcot/task/file/NIPS-2017-attention-is-all-you-need-Paper.pdf")
    documents = loader.load()

    # Create embeddings
    embeddings = OpenAIEmbeddings()
    text_splitter = CharacterTextSplitter(
          chunk_size=1000,
          chunk_overlap=0
          )
    docs = text_splitter.split_documents(documents)

    collection_name = "mytable"
    data_base = PGVector.from_documents(
        embedding=embeddings,
        documents=docs,
        collection_name=collection_name,
        connection_string=CONNECTION_STRING,
    )

    llm = ChatOpenAI(
            model_name='gpt-3.5-turbo',
            temperature=0.3,
            max_tokens=30
        )

    conversational_memory = ConversationBufferWindowMemory(
            memory_key='chat_history',
            k=10,
            return_messages=True
        )

    my_template = '''
               I want you to act as a "Attention-all-you-need" assistant.Give me correct answer of my question without adding other irrelevant information.
               Provide a valid and correct answer.You must have to give answers accordingly docs which i provided to you.It is mandatory for you to give 
               proper complete and correct answer of questions.If the user asks a greeting question then give helpful response.If a question which is
               irrelevant to this pdf then reply "Sorry I don't know, I am designed fora particular topic's information".Follow the instructions properly
               and strictly. 
               Context: {context} 
               Question: {question}
               Answer: 
               '''

    designed_prompt = PromptTemplate(template=my_template, input_variables=["context", "question"])
    chain_type_kwargs = {"prompt": designed_prompt}
    retrieval_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=data_base.as_retriever(),
            chain_type_kwargs=chain_type_kwargs,
            memory=conversational_memory
        )
    # Generate chat_system response using designed prompt
    try:
        response = retrieval_chain.run(user_ask)
    except openai.error.RateLimitError as rate_limit:
        return jsonify({'error':rate_limit})
    except openai.error.APIError as api_error:
        return jsonify({'error':api_error})
    except openai.error.APIConnectionError as api_connection:
        return jsonify({'error':api_connection})
    except openai.error.AuthenticationError as auth_error:
        return jsonify({'error':auth_error})
    except openai.error.Timeout as timeout_error:
        return jsonify({'error':timeout_error})
    except openai.error.ServiceUnavailableError as service_error:
        return jsonify({'error':service_error})
    except openai.error.InvalidRequestError as invalid_request:
        return jsonify({'error':invalid_request})
    except Exception as ex:
        return jsonify({'error':ex})
    return response
