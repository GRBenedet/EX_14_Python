#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from operator import itemgetter

jogadores = {}
rank = []
for c in range(0 , 4):
    i = str(input('nome do jogador: '))
    jogadores[i] = randint(1 , 6)

rank = sorted(jogadores.items(), key=itemgetter(1) , reverse=True)
print()
print(f'{'=' * 5} RANKING {'=' * 5}')
for i , c in enumerate(rank):
    print(f'{i + 1}ª lugar: {c[0]} com {c[1]} no dado')

