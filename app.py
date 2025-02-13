import streamlit as st
from services.vector_store import VectorStoreManager
from services.chat_service import ChatService
from utils.pdf_processor import process_pdf
from config.settings import MODEL_OPTIONS

def initialize_session():
    if 'messages' not in st.session_state:
        st.session_state['messages'] = []

def setup_ui():
    st.set_page_config(page_title='Chat JP', page_icon='🤖')
    st.header('🤖 Chat com seus documentos (RAG)')

def setup_sidebar():
    with st.sidebar:
        st.header('Upload de arquivos 📤')
        uploaded_files = st.file_uploader(
            label='Faça o upload de arquivos pdf',
            type=['pdf'],
            accept_multiple_files=True
        )
        
        selected_model = st.selectbox(
            label='Selecione o modelo LLM',
            options=MODEL_OPTIONS
        )
        
        return uploaded_files, selected_model

def main():
    initialize_session()
    setup_ui()
    
    vector_store = VectorStoreManager.load_existing()
    uploaded_files, selected_model = setup_sidebar()

    if uploaded_files:
        with st.spinner('Processando...'):
            all_chunks = []
            for uploaded_file in uploaded_files:
                chunks = process_pdf(file=uploaded_file)
                all_chunks.extend(chunks)
            vector_store = VectorStoreManager.add_documents(
                chunks=all_chunks,
                vector_store=vector_store
            )

    question = st.chat_input('Como posso ajudar?')

    if vector_store and question:
        for message in st.session_state.messages:
            st.chat_message(message.get('role')).write(message.get('content'))

        st.chat_message('user').write(question)
        st.session_state.messages.append(
            {'role': 'user', 'content': question}
        )

        with st.spinner('Pesquisando...'):
            response = ChatService.ask_question(
                model=selected_model,
                query=question,
                vector_store=vector_store
            )

        st.chat_message('ai').write(response)
        st.session_state.messages.append(
            {'role': 'ai', 'content': response}
        )

if __name__ == "__main__":
    main()