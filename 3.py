import random
nome = input("Escreva seu nome: ")
sobrenome = input("Escreva seu sobrenome: ")

lista_para_combinacao = ['jorge', 'schmuchk', 'kinsly', 'stark', 'lannister', 'juntschuk', 'randall', 'chunklackt', 'O incrivel', 'o corajoso', 'o determinado', 'eduardo', 'fernandes', 'filho', 'sá']

lista_para_combinacao.append(nome)

modificando_nome = (nome ,  sobrenome ,  random.choice(lista_para_combinacao))

novo_nome = " ".join(modificando_nome)

print(novo_nome)