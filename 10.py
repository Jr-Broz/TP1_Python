import random

personagens = ['João', 'Maria', 'Pedro', 'ricardo', 'marcos']
acoes = ['encontrou um alienigena', 'descobriu a cura de um virus que transforma os outros em zumbi', 'perdeu o celular', 'aprendeu a voar']
locais = ['na montanha', 'no espaco', 'na chapelaria', 'na van', 'no riacho']


personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)


historia = (f"{personagem} {acao} {local} ")

print("História: ")
print(historia)
