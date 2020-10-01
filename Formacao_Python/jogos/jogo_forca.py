def jogar():
    print("**************************")
    print("Bem vindo ao Jogo da forca")
    print("**************************")

    palavra_secreta = "banana"
    letras_descobertas = ["_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    #enquanto True and True
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_descobertas[index] = letra
            index += 1
        print(letras_descobertas)

    print("Fim do Jogo")

if(__name__=="__main__"):
    jogar()