# Chat Bot

This is chat boat.
It provides you information related to a pdf file.
Here you have to upload a pdf whose information you want.It act as a assistant which gives you answer of your question.Remember the questions you want to ask must be relevant to your pdf file, it will not give unnecessary or irrelevent information.


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

**$ pip install -r requirements.txt**

## Install PGVector Extension

Also configure postgresql database to connect with PGvector
Run below commands to install required extensions related to PGVectors -

**$ sudo apt-get install vector**

**$CREATE EXTENSION vector;**

## Run Chat Bot 

To run the chat bot, run api.py file in the terminal using the below command:

**python api.py**
