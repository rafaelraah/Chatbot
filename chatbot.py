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

# Histórico da conversa
messages = [

    {
        "role": "system",
        "content": "Você é um assistente amigável e inteligente."
    }

]

print("Chatbot com memória iniciado!")
print("Digite 'sair' para encerrar.\n")

while True:

    pergunta = input(f"{Fore.GREEN}Você: {Style.RESET_ALL} ")

    if pergunta.lower() == "sair":
        break

    # adicionar a pergunta do usuário 
    messages.append(
        {
            "role": "user",
            "content": pergunta
        }
    )

    # Chamada API
    response = client.chat.completions.create(

        model="openai/gpt-oss-120b",

        messages=messages

    )

    resposta = response.choices[0].message.content

    # Adiciona resposta do bot na memória
    messages.append(
        {
            "role": "assistant",
            "content": resposta
        }
    )

    print(f"{Fore.BLUE}Bot: {Style.RESET_ALL}" , resposta)
    print()