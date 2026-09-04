from urllib import response

from langchain_core import output_parsers
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
      ("system", "You are a helpful assistant. Respond to the user queries"),
      ("user", "Question: {question}")
    ]
)

llm = ChatOllama(model="llama3.1:8b")

def generate_response(question, llm, temperature, max_tokens):

   output_parser=StrOutputParser()
   chain = prompt|llm|output_parser
   answer = chain.invoke({'question':question})
   return answer

st.title("Enhanced QA Chatbot")
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.6)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=300, value=150)


st.write("Go ahead and ask your question")
user_input = st.text_input("You: ")

if user_input:
   response = generate_response(user_input,llm,temperature,max_tokens)
   st.write(response)
else:
   st.write("Please provide the query")