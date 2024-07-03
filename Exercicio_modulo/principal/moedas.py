def aumentar(n, formato=False):
    calculo=(n/100)*150
    return calculo if formato is False else moeda(calculo)


def subtração(n,formato=False):
    calculo=(n/100)*80
    return calculo if formato is False else moeda(calculo)


def divisão(n,formato=False):
    div=n/2
    return div if formato is False else moeda(div)


def dobro(n,formato=False):
    dob=n*2
    return dob if formato is False else moeda(dob)


def moeda(n):
    converter=str(n)
    cigla="R$"+converter
    return cigla

