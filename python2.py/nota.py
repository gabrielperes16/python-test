ficha=list()
cont=0
while True:
    cont+=1
    nome=str(input("Digite seu nome: "))
    nota1=float(input("Digite sua nota 1: "))
    nota2=float(input("Digite sua nota 2: "))
    media=(nota1+nota2)/2
    ficha.append(nome,[nota1,nota2], media)
    conti=str(input("Quer continuar [ s ] ou [ n ]: ").lower())
    if conti == 'n':
        break
print("-="*40)
print(f'{"No.:<4"} {"NOME:<10"} {"MÉDIA":>8}')
print('-'*26)
print(f"{ficha}")
for i, a in enumerate(ficha):
    print(f"{}{}{}")












