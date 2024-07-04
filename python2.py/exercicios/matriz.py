matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = scoluna = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input("Digite um valor:"))
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c] ^ 5}]", end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
    print()
print(f"A soma dos valorez é {pares}")
for l in range(0,3):
    scoluna+=matriz[l][2]
print(f"A soma dos valores da coluna 2 é {scoluna}")
for c in range(0,3):
    if c==0:
        maior=matriz[1][c]
    elif matriz[1][c] > maior:
        maior=matriz[1][c]
print(f'o maior valor é {maior}')