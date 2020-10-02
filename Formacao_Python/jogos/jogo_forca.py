def jogar():
    print("**************************")
    print("Bem vindo ao Jogo da forca")
    print("**************************")

    palavra_secreta = "banana".upper()
    letras_descobertas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False
    erros = 0

    #enquanto True and True

    print(letras_descobertas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_descobertas[index] = letra
                index += 1
        else:
            erros += 1
        enforcou = erros == 6
        acertou = "_" not in letras_descobertas
        print(letras_descobertas)

    if(acertou):
        print("Parabéns! Você ganhou o jogo.")
    else:
        print("Você perdeu!")

    print("Fim do Jogo")

if(__name__=="__main__"):
    jogar()