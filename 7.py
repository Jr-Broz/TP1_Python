def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def ler_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obeso"

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = calcular_imc(peso, altura)
interpretacao = ler_imc(imc)

print(f"Seu imc é {imc:.2f}. Você está {interpretacao}.")
