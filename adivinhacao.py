import random


print("*********************************")
print("Bem vindo no jogo de Adivinhação!")
print("*********************************")


# numero_secreto = round(random.random() * 100) # 0.0 1.0
numero_secreto = random.randrange(1, 101) # 1 a 100
total_de_tentativas = 0
pontos = 1000

print("Qual nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

# rodada = 1

# print(numero_secreto)

# while (rodada <= total_de_tentativas):

for rodada in range(1, total_de_tentativas + 1):

    # print(f"Tentantiva {rodada} de {total_de_tentativas}")

    #                           String interpolation
    print("Tentantiva {} de {}".format(rodada, total_de_tentativas))

    chute_str = input("Digite o seu número: ")
    print("Você digitou ", chute_str)

    chute = int(chute_str)

    if (chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    # Logica
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Você acertou e fez {} pontos!!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor do que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

# print("Você errou")

print("Fim do jogo")

