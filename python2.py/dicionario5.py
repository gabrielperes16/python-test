info={}
cadastros=media=soma=0
pessoal=list()
while True:
    info.clear()
    cadastros+=1
    info['nome']=str(input("digite o nome: "))
    while True:
        info['sexo']=str(input("Digite seu sexo [ M ] ou [ F ]: ").upper()[0])
        if info['sexo']  in 'MF':
            break
        print("Erro! escreva apenas M ou F ")
    info['idade']=int(input("Digite sua idade: "))
    soma+=info['idade'] 
    pessoal.append(info.copy())
    while True:
        continuar=str(input("Quer continuar [ S ] ou [ N ]").upper()[0])
        if continuar in 'SN':
            break
        print("Erro! escreva apenas [S] ou [N]")
    if continuar =='N':
        break
media=(soma/cadastros)
for p in pessoal:
    if p['sexo'] in 'Ff':
        print(f"{p['nome']}", end="")
print()
print("-="*20)
print(f'A quantidade de pessoas cadastradas é de {cadastros}')
print("-="*20)
print(f"A media de idade é de {media}")
print("-="*20)
print("Listas das pessoas que estão acima da média: ", end="")
for p in pessoal:
    if info["idade"]>=media:
        print("       ")
        for k,v in p.items():
            print(f"{k}={v};", end='')
        print()
print("ENCERRADO")
            





