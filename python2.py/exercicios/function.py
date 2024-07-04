def calculo(larg, comp):
    area = larg*comp
    print(f"A Area do terreno é de {larg}x{comp}={area}")


larg = float(input("Digite a largura da area: "))
comp = float(input("Digite o comprimento da area: "))
calculo(larg, comp)
