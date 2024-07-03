import moedas
n=int(input("Digite o valor:"))
print(f"O valor de {n} + 50% é igual a: {moedas.aumentar(n)}")
print(f'o valor {n} - 20% é igual a: {moedas.subtração(n)}')
print(f"Apos a divisão de {n} por 2 o valor é igual a:{moedas.divisão(n)}")
print(f"O valor {n} multiplicado por 2 é igual a: {moedas.dobro(n)}")
