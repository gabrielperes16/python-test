info={}
while True:
    info['nome']=str(input("digite o nome: "))
    info['sexo']=str(input("Digite seu sexo [ M ] ou [ F ]: ").upper()[0])
    if info['sexo']  in 'MF':
        break
    print("Erro! escreva apenas M ou F ")  
    info['idade']=int(input("Digite sua idade: "))
    continuar=str(input("Quer continuar [ S ] ou [ N ]").upper())
while True:
    if continuar in 'SN':
        break
    print("Erro! escreva apenas [S] ou [N]")
print(info)

