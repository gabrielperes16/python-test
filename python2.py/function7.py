def fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(" X ", end='')
            else:
                print(" = ", end='')
        f *= c
    return f


valor = int(input("Qual valor você vai querer? "))
print(fatorial(valor, show=True))
