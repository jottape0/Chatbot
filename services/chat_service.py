import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from config.settings import SYSTEM_PROMPT

class ChatService:
    @staticmethod
    def ask_question(model, query, vector_store):
        """Process question and return answer."""
        llm = ChatOpenAI(model=model)
        retriever = vector_store.as_retriever()

        messages = [('system', SYSTEM_PROMPT)]
        for message in st.session_state.messages:
            messages.append((message.get('role'), message.get('content')))
        messages.append(('human', '{input}'))

        prompt = ChatPromptTemplate.from_messages(messages)
        question_answer_chain = create_stuff_documents_chain(
            llm=llm,
            prompt=prompt
        )

        chain = create_retrieval_chain(
            retriever=retriever,
            combine_docs_chain=question_answer_chain
        )

        response = chain.invoke({'input': query})
        return response.get('answer')