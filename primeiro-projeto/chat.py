import os

mensagens = []

nome = input("Nome: ")

while True:
    os.system("clear")

    print("Para sair do chat digite 'fim'")
    
    if len(mensagens) > 0:
        for msg in mensagens:
            print(msg['nome'], "-" ,msg['texto'])
    print("_________________________")

    texto = input("Digite sua mensagem: ")
    if texto == "fim":
        break

    mensagens.append({"nome": nome, "texto": texto})