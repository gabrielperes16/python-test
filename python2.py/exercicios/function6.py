def voto(ano):

    from datetime import date
    ano_atual = date.today().year
    idade=  ano_atual-ano
    if idade<16:
        return "O voto foi negado"
    elif idade>=16 and idade<18:
        return "O voto é opcioanl"
    elif idade>18:      
        return "O voto é obrigatorio!"
nasc=int(input("Em que ano voce nasceu? "))
print(voto(nasc))




