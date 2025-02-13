import os
from decouple import config

# Environment variables
OPENAI_API_KEY = config('OPENAI_API_KEY')
os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

# Application settings
PERSIST_DIRECTORY = 'db'
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 400

# Model options
MODEL_OPTIONS = [
    'gpt-3.5-turbo',
    'gpt-4',
    'gpt-4-turbo',
    'gpt-4o-mini',
    'gpt-4o'
]

# Prompts
SYSTEM_PROMPT = '''
Use o contexto para responder as perguntas.
Se não encontrar uma resposta no contexto,
explique que não há informações disponíveis.
Responda em formato de markdown e com visualizações
elaboradas e interativas.
Contexto: {context}
'''