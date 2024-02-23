def votacao():

    opcao1_votos = 0
    opcao2_votos = 0
    opcao3_votos = 0

    while True:
        print("Escolha uma opcao: ")
        print("1. Opção 1 ")
        print("2. Opção 2 ")
        print("3. Opção 3 ")
        print("0. Encerrar a votação ")
        voto = input("Digite o número da opção  ou 0 para encerrar: ")

        if voto == '1':
            opcao1_votos += 1
        elif voto == '2':
            opcao2_votos += 1
        elif voto == '3':
            opcao3_votos += 1
        elif voto == '0':
            break
        else:
            print("Error, tente novamente!")

    print("\nResultado da votação:")
    print("Opção 1:", opcao1_votos, "votos")
    print("Opção 2:", opcao2_votos, "votos")
    print("Opção 3:", opcao3_votos, "votos")

votacao()