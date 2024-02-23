def minutos_para_horas_minutos(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return horas, minutos

#=====================================================
minutos = int(input("Digite o total de minutos: "))
horas, minutos_restantes = minutos_para_horas_minutos(minutos)

print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")

