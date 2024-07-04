from random import randint
from time import sleep
print("=="*15)
print("       JOGO DA MEGA SENA")
print("=="*15)
num = int(input("Quantos jogos você quer jogar?"))
lista = list()
jogos=list()
total=0
while total <= num:
    cont=0
    while True:
        valor = randint(1, 60)
        if valor not in lista:
            lista.append(valor)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total+=1
print("\033[32mCARREGANDO....\033[m")
sleep(1)
for i, l in enumerate(jogos):
    sleep(0.8)
    print(f'jogo {i+1}: {l}')
