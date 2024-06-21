ficha=list()
cont=0
while True:
    cont+=1
    nome=str(input("Digite seu nome: "))
    nota1=float(input("Digite sua nota 1: "))
    nota2=float(input("Digite sua nota 2: "))
    media=(nota1+nota2)/2
    ficha.append([nome,[nota1,nota2], media])
    conti=str(input("Quer continuar [ s ] ou [ n ]: ").lower())
    if conti == 'n':
        break
print("-="*20)
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
while True:
    most_nota= int(input("Mostrar nota de qual aluno? (999)interrompe: "))
    if most_nota == 999:
        break
    if most_nota <= len(ficha)-1:
            print(f"Notas de {ficha[most_nota][0]} são {ficha[most_nota][1]}")
print(f"\033[32mPROGRAMA FINALIZADO!\033[m")

