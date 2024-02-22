def historia():
    print("vc esta numa floresta")
    escolha = input("Você vai pra esquerda ou para a direita? ")

    if escolha.lower() == "esquerda":
        print("vc foi pra esquerda  esquerda e achou um tesouro!")
    elif escolha.lower() == "direita":
        print("vc foi pra direita e encontra um dragao")
    else:
        print("Você fica parado e é devorado por lobos.")

historia()
