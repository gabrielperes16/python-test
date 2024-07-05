import modulo

modulo.decoracao(msg='\033[32mMENU PRINCIPAL\033[m'.center(67))
escolha = modulo.menu()
print(f"Você escolheu a opção: {escolha}")