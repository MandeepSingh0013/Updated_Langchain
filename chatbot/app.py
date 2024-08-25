from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
##Langsmith Tracking 
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

#Promt Template

prompt= ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please response to the users queries in short or precies"),
        ("user", "Question:{question}")
    ]
)

#Streamlit framework
st.title("Langchain Feature Exporation With Open API")
input_text=st.text_input("search The Topic You Want")

#Open 
llm= ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))