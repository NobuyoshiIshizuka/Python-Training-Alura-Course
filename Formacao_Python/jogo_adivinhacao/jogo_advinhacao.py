print("*********************************")
print("Bem vindo ao jogo de adivinhacao!")
print("*********************************")

numero_secreto = 50
chute_str = input("Digite um número para tentar advinhar o numero secreto:")
print("Você digitou ", chute_str)
chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    print("Você errou!")

