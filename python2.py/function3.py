from time import sleep


def maior(*num):
    cont = maior = 0
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f"{valor} ", end='', flush=True)
        sleep(0.3)
    maior_valor = max(num)
    print(f"\nO maior valor informado foi {maior_valor}.")  

maior(2, 9, 4, 5, 7, 1)
maior(4,7,0)
maior(1,2)
maior(6)

