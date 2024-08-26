from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
#Promt Template

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the users queries in short or precies"),
        ("user", "Question:{question}")
    ]
)

#Streamlit framework
st.title("Langchain Feature Exporation With LLAMA 2")
input_text=st.text_input("search The Topic You Want")

#Calling LLama 2
#Go to command promt and type 'ollama run gemma' it will doenload the model and then you are able to use it localy
llm= ollama(model='llama2')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser