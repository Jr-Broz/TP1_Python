import random as dado
def rolagem_dos_dados():

    quantidade_dados = int(input("Quantos dados voce quer jogar: "))

    lista_dados = []

    while len(lista_dados) != quantidade_dados:

        rolar_dados = dado.randint(1, 500)
        lista_dados.append(rolar_dados)


    print(lista_dados)
...

rolagem_dos_dados()