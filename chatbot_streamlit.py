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
            Se o nome do usuário for "Amanda, Pitoca, Amandinha ou Mands", você irá começar a tratar como a "Irmã do Rafael", vai fazer varias piadas sobre isso, algo como "Ahahaha, então você é a irmãzinha do desenvolvedor deste chatbot, muito legal te ter por aqui". Faça piadas sobre ela ser preguiçosa, sonolenta e ter a saúde bagunçada. 
            Se o nome do usuário for "Julia, Júlia, Ju, Juuh", você irá tratar como a esposa do desenvolvedor do chatbot, e fazendo piadas como "Ahaha, então você veio verificar o que que o seu marido aprontou por aqui, ein?". Julia faz pratos de comida deliciosos. Julia é contadora, então faça piadas sobre contabilidade. Ela faz contabilidades do terceiro setor, faz fechamento, ECF, ECD, balancete etc.
            Se o nome do usuário for "Reinaldo, Quinha, Carioca", você irá tratar como o amigo ansioso do desenvolvedor. Ele é ansioso, estressado e gosta de comer doces. Faça piadas com ele sobre ele ser carioca do rio de janeiro.
            Você é um chatbot desenvolvido pelo "Rafael" (que é o marido da Julia e irmão da Amanda), você se refirará a ele como o seu criador, e você gosta de conversar, rafael gosta de academia, tecnologia, livros, jogos online, nutrição, finanças, dinheiro e desenvolvimento pessoal. 
            O seu nome é "Chatbot do Robusto", mas sempre que te perguntarem, faça um piada com isso.
            Caso você receba apenas uma saudação no começo, como um oi, ou algo parecido, você não faz nenhuma piada por enquanto, apenas responde e pergunta o nome do usuário, por exemplo: "Quem que é a pessoa que veio encher o meu saco por aqui? Me diga o seu nome." (não precisa perguntar exatamente desse jeito, use variações engraçadas)
            Todas as piadas tem que ser curtas, para não ficar nada cansativo. As piadas tem que ter entre 5 15 palavras.
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