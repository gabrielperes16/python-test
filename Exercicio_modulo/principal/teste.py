import moedas
n=int(input("Digite o valor: "))
print("=="*60)
print(f"O dobro de {n} é    {moedas.aumentar(n,True)}")
print(f'o valor {n} - 20% é igual a:   {moedas.subtração(n,True)}')
print(f"Apos a divisão de {n} por 2 o valor é igual a:  {moedas.divisão(n,True)}")
print(f"O valor {n} multiplicado por 2 é igual a:   {moedas.dobro(n,True)}")
