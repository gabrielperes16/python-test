from time import sleep
def linha():
    print("=="*20)


def contador(i, f, p):
    print(f"Contagem de {i} ao {f} em {p} em {p}")


    if i <= f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=' ',flush=True)
            sleep(0.5)
            cont += p
        print("FIM")
        
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=' ',flush=True)
            sleep(0.5)
            cont -= p
        print("FIM")
    linha()

linha()
contador(1, 10, 1)
contador(10,0,2)
personalizado=str(input("Quer personalizar?   [ S ] ou [ N ]: ")).upper()
if personalizado == 'S':
    n1=int(input("Insira o valor inicial: "))
    n2=int(input("Valor final: "))
    n3=int(input("De quantos em quantos?  "))
linha()
contador(n1,n2,n3)
