from datetime import datetime
informaçoes = {}
informaçoes['nome'] = str(input("Digite seu nome: "))
informaçoes['anos nascimento'] = int(input("Digite o Seu ano de nascimento: "))
informaçoes['carteira de trabalho'] = int(
    input("Carteiro de trabalho ( 0 Não tem ): "))
if informaçoes['carteira de trabalho'] != 0:
    informaçoes['ano contratação'] = int(
        input("Digite o ano de contratação: "))
    informaçoes['salario'] = int(input("Digite seu salario: "))
    informaçoes['aposentadoria'] = informaçoes['anos nascimento'] + ((informaçoes['ano contratação'] + 35) - 2024)
print("-="*20)
for k, v in informaçoes.items():
    print(f"    - {k} tem o valor de {v}")
print("-="*20)
