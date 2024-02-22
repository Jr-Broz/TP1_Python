def minutos_para_horas_minutos(total_minutos):
    horas = total_minutos // 60
    minutos = total_minutos % 60
    return horas, minutos


def horas_minutos_para_minutos(horas, minutos):
    total_minutos = horas * 60 + minutos
    return total_minutos


#=====================================================
minutos = int(input("Digite o total de minutos: "))
horas, minutos_restantes = minutos_para_horas_minutos(minutos)

print(f"{minutos} minutos equivalem a {horas} horas e {minutos_restantes} minutos.")


#=======================================

horas = int(input("Digite o total de horas: "))
minutos = int(input("Digite o total de minutos: "))
total_minutos = horas_minutos_para_minutos(horas, minutos)
print(f"{horas} horas e {minutos} minutos equivalem a {total_minutos} minutos.")
