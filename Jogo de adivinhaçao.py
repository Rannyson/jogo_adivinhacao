
import random

palavra = ['Faca','Garfo','Cachorro','teclado']
teste = palavra[random.randrange(0, len(palavra))-1]
for x in range(100):
    print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""
    for letra in teste:
        senha += letra if letra in acertos else "."
    print(senha)
    if senha == teste:
        print("Você acertou!")
        break
    tentativa = input("\nDigite uma letra:").lower().strip()
    if tentativa in digitadas:
        print("Você já tentou esta letra!")
        continue
    else:
        digitadas += tentativa
        if tentativa in teste:
            acertos += tentativa
        else:
            erros += 1
            print("Você errou!")
    print("X==:==\nX  :   ")
    print("X  O   " if erros >= 1 else "X")
    linha2 = ""
    if erros == 2:
        linha2 = "  |   "
    elif erros == 3:
        linha2 = " \|   "
    elif erros >= 4:
        linha2 = " \|/ "
    print("X%s" % linha2)
    linha3 = ""
    if erros == 5:
        linha3 += " /     "
    elif erros >= 6:
        linha3 += " / \ "
    print("X%s" % linha3)
    print("X\n===========")
    if erros == 6:
        print("Enforcado jogador de free fire!")
        break
