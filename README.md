# Chat JP - Chat com seus documentos (RAG)

## Descrição
Chat JP é uma aplicação que permite interagir com documentos PDF utilizando um modelo de aprendizado de máquina (LLM). O sistema processa documentos, extrai informações relevantes e permite ao usuário fazer perguntas sobre o conteúdo dos arquivos.

## Tecnologias Utilizadas
- **Python**
- **Streamlit** (Interface)
- **VectorStoreManager** (Gerenciamento de embeddings)
- **ChatService** (Interação com o modelo LLM)
- **PDF Processing** (Extração de textos de PDFs)

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
```

### 2. Criar e Ativar o Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3. Instalar as Dependências
```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação
```bash
streamlit run app.py
```

## Como Utilizar
1. **Faça o seu cadastro na plataforma da OPENAI para obter a API_SECRET_KEY 
2. **Upload de Arquivos**: Envie arquivos PDF através da barra lateral.
3. **Seleção de Modelo**: Escolha um modelo de LLM para processar as perguntas.
4. **Interação**: Digite sua pergunta no campo de chat e obtenha respostas baseadas no conteúdo do documento.

## Estrutura do Projeto
```
├── app.py
├── services
│   ├── vector_store.py
│   ├── chat_service.py
├── utils
│   ├── pdf_processor.py
├── config
│   ├── settings.py
├── requirements.txt
├── README.md
```

