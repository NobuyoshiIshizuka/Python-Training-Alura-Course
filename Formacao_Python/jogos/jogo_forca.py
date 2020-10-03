import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_descobertas = inicializa_letras_descobertas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    #enquanto True and True

    print(letras_descobertas)

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
           marca_chute_correto(chute, letras_descobertas, palavra_secreta)
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_descobertas
        print(letras_descobertas)

    if(acertou):
       imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()

def imprime_mensagem_vencedor():
    print("Você ganhou!")


def imprime_mensagem_perdedor():
    print("Você perdeu")

def marca_chute_correto(chute, letras_descobertas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_descobertas[index] = letra
        index += 1

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def imprime_mensagem_abertura():
    print("**************************")
    print("Bem vindo ao Jogo da forca")
    print("**************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r", encoding="utf-8")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_descobertas(palavra):
  return ["_" for letra in palavra]

if(__name__=="__main__"):
    jogar()