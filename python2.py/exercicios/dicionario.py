dicionario=dict()
dicionario['nome']=str(input("Digite seu nome: "))
dicionario['media']=float(input("Digite sua media: "))
print("=="*10)
print(f"Nome é igual a {dicionario['nome']}")
print(f"A sua media é igual a {dicionario['media']}")
if dicionario['media'] < 7:
    print("Sua situação é Reprovado")
elif dicionario['media'] >= 7:
    print("Sua situação é Aprovado!")
print("=="*10)