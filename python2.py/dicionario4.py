time=list()
jogador = {}
partidas= []
while True:
    jogador.clear()
    jogador['nome'] = str(input("Digite o nome do jogador: "))
    tot=int(input("Quantas partidas este jogador jogou?"))
    for c in range(0, tot):
        partidas.append(int(input("Digite a quantidade de gols: ")))
    jogador['gols']=partidas[:]
    jogador['total']=sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar=str(input("Quer continuar?  [ S ] ou [ N ]")).upper()[0]
        if continuar in "SN":
            break
        print("Responda corretamente!")
    if continuar=='N':
        break
print("-="*30)
print("Cod", end='')
for i in jogador.keys():
    print(f"{i:<15}", end='')
print()
print("-"*40)
for k,v in enumerate(time): 
    print(f'{k}     ',end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
print("-"*40)
while True:
    busca=int(input("MOstra os dados de qual jogador:"))
    if busca == 999:
        break
    if busca >= len(time):
        print("Jogador não encontrado!")
    else:
        print(f"-- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
        for i,g in enumerate(time[busca]['gols']):
            print(f"        no jogo {i} fez {g} gols")
        print('=='*30)
