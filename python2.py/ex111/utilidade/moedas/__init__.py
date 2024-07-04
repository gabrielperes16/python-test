def aumentar(n, formato=False):
    calculo = (n/100)*120
    return calculo if formato is False else moeda(calculo)


def subtração(n, formato=False):
    calculo = (n/100)*88
    return calculo if formato is False else moeda(calculo)


def divisão(n, formato=False):
    div = n/2
    return div if formato is False else moeda(div)


def dobro(n, formato=False):
    dob = n*2
    return dob if formato is False else moeda(dob)


def moeda(n):
    converter = str(n)
    cigla = "R$"+converter
    return cigla


def resumo(n):
    print("=="*30)
    print("RESUMO VALOR".center(53))
    print("=="*30)
    print(f'''
        Preço analisado:    {moeda(n)}
        Dobro do preço:     ({moeda(dobro(n, True))})
        Metade do preço:    {moeda(subtração(n, True))}
        20%  de aumento:    {moeda(aumentar(n, True))}
        12%  de Redução:    {moeda(subtração(n, True))}
    ''')
    print("=="*30)
