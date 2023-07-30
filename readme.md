# Chat Bot

An implementation of a chatbot using OpenAI language model GPT-3.5
It provides you the required information related to a pdf file.
User needs to upload a pdf to get the required information from it.This act as an assistant which gives the answers for the queries related to the uploaded pdf.The queries must be related to the submitted pdfs, currently system is not capable to answer the irrelated queries.

![LangChain_chatBot](https://github.com/choudhary-sumer/chat_bot/assets/140950427/5471ede3-91c4-4a37-a5e7-75c4639a93d1)




# Installation

Follow below steps to install **Chat Bot!**

## Create Virtual Environment

Run below command to create a virtual environment -

**$ python3 -m venv $name**

## Activate the virtual environment
Run the activate script present in bin folder under the created environment -

**$ ./$name/bin/activate**

## Install the requirements

All the dependencies mentioned in the requirements.txt file must be installed before running the code base -
Do not forget to add secret key in .env file  OPENAI_API_KEY="api_key".
You can generate an api key by using this https://www.openai.com/

**$ pip install -r requirements.txt**

## Install PGVector Extension

Also configure postgresql database to connect with PGvector
Run below commands to install required extensions related to PGVectors -

**$ sudo apt-get install vector**

**$CREATE EXTENSION vector;**

## Run Chat Bot 

To run the chat bot, run api.py file in the terminal using the below command:

**python api.py**
