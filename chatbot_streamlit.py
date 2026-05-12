import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from colorama import Fore, Style, init
import os

# Carrega variáveis do .env
load_dotenv()

# Cliente Groq
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Memória
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "system",
            "content": "Você é um assistente amigável."
        }
    ]

# Título
st.title("Robusto Chatbot")

# Mostrar mensagens antigas
for msg in st.session_state.messages:

    if msg["role"] != "system":

        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# Input do usuário
prompt = st.chat_input("Digite sua mensagem")

if prompt:

    # Mostra usuário
    with st.chat_message("user"):
        st.write(prompt)

    # Salva pergunta
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Chamada API
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=st.session_state.messages
    )

    resposta = response.choices[0].message.content

    # Mostra resposta
    with st.chat_message("assistant"):
        st.write(resposta)

    # Salva memória
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": resposta
        }
    )