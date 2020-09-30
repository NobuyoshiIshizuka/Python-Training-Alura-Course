import random

print("*********************************")
print("Bem vindo ao jogo de adivinhacao!")
print("*********************************")

numero_secreto = random.randrange(1,100)
total_de_tentativas = 0
rodada = 1

print("Qual o nível de dificuldade?")
print("(1) Fácil, (2)Médio, (3)Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1 or nivel == 2 or nivel == 3):
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):
        total_de_tentativas = 5
else:
    print("Nível definido inválido")
print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acertou = (chute == numero_secreto)
    maior   = (chute > numero_secreto)
    menor   = (chute < numero_secreto)

    if(acertou):
        print("Você acertou!")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto")

print("Fim do jogo")



