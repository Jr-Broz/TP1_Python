import random

numero_aleatorio = random.randint(1,15)
numero_tentativas = 3


while numero_tentativas != 0:

    guess = int(input('guess the number: '))

    if guess == numero_aleatorio:
        print(f"Muito bem vc acertou o numero era {numero_aleatorio}")
        break

    if guess > numero_aleatorio:
        numero_tentativas -= 1
        print("vc tentou adivinhar muito pra cima")


    if guess < numero_aleatorio:
        numero_tentativas -= 1

        print("Voce tentou adivinhar muito pra baixo")

    if numero_tentativas == 0:
        print(f"Acabou suas chances! , o numero era {numero_aleatorio}")
