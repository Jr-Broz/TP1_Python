import random

personagens = ['João', 'Maria', 'Pedro', 'Ana', 'Carlos']
acoes = ['encontrou um mapa', 'descobriu um tesouro', 'perdeu um objeto valioso', 'foi em busca de aventuras', 'ajudou um estranho']
locais = ['na montanha', 'em uma cidade antiga', 'no fundo do mar', 'em um castelo abandonado', 'no riacho']


personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)


historia = (f"{personagem} {acao} {local}.")

print("História: ")
print(historia)
