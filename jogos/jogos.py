import jogo_adivinhacao
import jogo_forca

def escolhe_jogo():
    print("***************************")
    print("****Escolha o sue jogo!****")
    print("***************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        jogo_forca.jogar()
    elif(jogo == 2):
        print("Jodando adivinhação")
        jogo_adivinhacao.jogar()

if(__name__=="__main__"):
    escolhe_jogo()
