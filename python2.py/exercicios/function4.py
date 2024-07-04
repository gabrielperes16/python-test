from random import randint
from time import sleep
def sorteia(lista):
    for cont in range(0,5):
        lista.append(randint(1,5))
        sleep(0.2)
    print(f"Os numeros sorteados foram {numero}")


def valorPar(par):   
    for valor in numero:
        if valor%2==0:
            par.append(valor)
            sleep(0.5)
    print(f"A lista de numeros pares é {pares}")


pares=list()
numero=list()
sorteia(numero)
valorPar(pares)
