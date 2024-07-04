def jogador(nome='<Desconhecido>', gols=0):
    print(f"O jogador   {nome}  fez {gols} gols no campeonato.")

n = str(input("Qual o nome do jogador: "))
if not  n:
    n="<Desconhecido>"

g = int(input("Quantos gols ele fez no campeonato: "))
jogador(n, g)
