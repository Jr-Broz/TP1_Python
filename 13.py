palavra = input("escreve: ")

palindromo = palavra[:: -1]

if palavra == palindromo:

    print("O reverso fica:" , palindromo)
    print("É um palindromo")

else:
    print("nao e palindromo")

    #Exemplos de palindromos: Ana, Nathan, Oto e Hanah