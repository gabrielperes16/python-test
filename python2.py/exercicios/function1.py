def escreva(txt):
    tam=len(txt)+4
    print("~"*tam)
    print(f'  {txt}')
    print("~"*tam)

fala=str(input("fale: "))
escreva(fala)