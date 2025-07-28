import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "AIzaSyC3w6jUXUz7Vx9YULWbe-4aQNUW_RX6JMQ"  # replace with your actual key

# Streamlit UI
st.title(" AI Chatbot using LangChain")
context = st.text_area("Paste context or information the bot should know:", height=250)
question = st.text_input("Ask your question:")

if st.button("Get Answer"):
    if not context or not question:
        st.warning("Please enter both context and a question.")
    else:
        llm = ChatOpenAI(temperature=0)
        prompt_template = """Use the following context to answer the question.

        Context: {context}
        Question: {question}
        Answer:"""
        PROMPT = PromptTemplate(
            input_variables=["context", "question"],
            template=prompt_template,
        )
        chain = LLMChain(llm=llm, prompt=PROMPT)
        response = chain.run({"context": context, "question": question})
        st.success(response)
