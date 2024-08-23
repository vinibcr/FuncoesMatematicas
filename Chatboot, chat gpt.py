import time
import openai

# Configuração da chave API
chave_api = "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"
openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )

    return resposta["choices"][0]["message"]

lista_mensagens = []
while True:
    texto = input("Escreva aqui sua mensagem:")

    if texto == "sair":
        break
    else:
        try:
            resposta = enviar_mensagem(texto, lista_mensagens)
            lista_mensagens.append(resposta)
            print("Chatbot:", resposta["content"])
        except openai.error.RateLimitError:
            print("Você excedeu o limite de requisições. Por favor, tente novamente mais tarde.")
            time.sleep(60)  # Aguarda 60 segundos antes de tentar novamente
