import os

def minha_funcao(valor1,valor2):
    return valor1 + valor2


while True:
    os.system("clear")
    resposta = minha_funcao(float(input("Digite um numero: ")),float(input("Digite outro numero: ")))
    print("Resposta: ", resposta)
    if input("Deseja continuar? (s/n): ") == "n":
        break