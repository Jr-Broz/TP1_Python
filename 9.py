compra = int(input("escreve o valor da compra: "))

if compra > 100:

    desconto = (compra * 10) /100
    novo_valor = compra - desconto
    print(f"Valor antigo {compra}  novo com desconto {novo_valor}")

elif compra > 250:

    desconto = (compra * 15)/100
    novo_valor = compra - desconto

    print(f"Valor antigo {compra}  novo valor com desconto {novo_valor}")


elif compra > 300:

    desconto = (compra * 35) / 100
    novo_valor = compra - desconto
    print(f"Valor antigo {compra}  novo valor com desconto {novo_valor}")