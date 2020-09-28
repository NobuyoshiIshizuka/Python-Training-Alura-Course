print("*********************************")
print("Bem vindo ao jogo de adivinhacao!")
print("*********************************")

numero_secreto = 50
chute_str = input("Digite um número para tentar advinhar o numero secreto:")
print("Você digitou ", chute_str)
chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if(acertou):
    print("Você acertou!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto")

