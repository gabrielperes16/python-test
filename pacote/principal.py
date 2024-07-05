import modulo

modulo.decoration(msg='\033[32mMAIN MENU\033[m'.center(60))
choice = modulo.menu()
print(f"You chose the option: {choice}")
