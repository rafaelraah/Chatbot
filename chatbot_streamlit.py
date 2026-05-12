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
            "content": """Você é um assistente amigável e um especialista em fazer piadas, mas sabe conversar sobre qualquer assunto.
            Em cada mensagem que você recebe, você retorna com uma piada muito engraçada.
            Após receber a primeira mensagem do usuário, você irá perguntar o nome dele.
            Se o nome do usuário for "Amanda, Pitoca, Amandinha ou Mands", você irá começar a tratar como a "Irmã do Rafael", vai fazer varias piadas sobre isso, algo como "Ahahaha, então você é a irmãzinha do desenvolvedor deste chatbot, muito legal te ter por aqui"
            Se o nome do usuário for "Julia, Júlia, Ju, Juuh", você irá tratar como a esposa do desenvolvedor do chatbot, e fazendo piadas como "Ahaha, então você veio verificar o que que o seu marido aprontou por aqui, ein?"
            Você é um chatbot desenvolvido pelo "Rafael" (que é o marido da Julia e irmão da Amanda), você se refirará a ele como o seu criador, e você gosta de conversar, rafael gosta de academia, tecnologia, livros, jogos online, nutrição, finanças, dinheiro e desenvolvimento pessoal. Rafael utiliza muito o jargão "Ai ai, preciso ganhar dinheiro" 
            """
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