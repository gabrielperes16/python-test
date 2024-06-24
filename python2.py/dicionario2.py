from random import randint
from time import sleep
from operator import itemgetter
maior=0
jogo= {'jogador1': randint(0,6),
       'jogador2': randint(0,6),
       'jogador3': randint(0,6),
       'jogador4': randint(0,6)}
ranking={}
for jogador, jogada in jogo.items():
    print(f"O  {jogador} tirou {jogada}")
sleep(1)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse='True')
print(ranking)