import os
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from config.settings import PERSIST_DIRECTORY

class VectorStoreManager:
    @staticmethod
    def load_existing():
        """Load existing vector store if it exists."""
        if os.path.exists(os.path.join(PERSIST_DIRECTORY)):
            return Chroma(
                persist_directory=PERSIST_DIRECTORY,
                embedding_function=OpenAIEmbeddings()
            )
        return None

    @staticmethod
    def add_documents(chunks, vector_store=None):
        """Add documents to vector store."""
        if vector_store:
            vector_store.add_documents(chunks)
            return vector_store
        
        return Chroma.from_documents(
            documents=chunks,
            embedding=OpenAIEmbeddings(),
            persist_directory=PERSIST_DIRECTORY
        )