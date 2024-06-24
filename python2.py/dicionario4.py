soma=0
registro={}
registro['nome']=str(input("Digite o nome do jogador: "))
registro['partidas']=int(input("Quantas partidas este jogador jogou?"))
for partida in range(1,registro['partidas']+1):
    registro['gols']=int(input("Digite a quantidade de gols: "))
    soma+=registro['gols']
registro['total']=soma
print("-="*30)
print(registro)
print("-="*30)
for k,v in registro.items():
    print(f"O campo {k} tem o valor {v}")
print("-="*30)
print(f"O jogador {registro["nome"]} jogou {registro['partidas']}")
for i, v in enumerate(registro['gols']):
    print(f"     => na partida {i}, fez {v} gols")
print(f"Foi um total de {registro['total']}gols")