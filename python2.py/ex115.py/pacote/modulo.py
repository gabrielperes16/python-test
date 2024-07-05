def decoracao(msg):
    print("\033[32m==\033[m" * 30)
    print(msg)
    print("\033[32m==\033[m" * 30)

def menu():
    print('''\033[36m
    1- Ver pessoas cadastradas
    2- Cadastrar Nova pessoa
    3- Sair do sistema\033[m
''')
    print("\033[32m==\033[m" * 30)
    escolha = validador("Sua Escolha: ")
    if escolha == 3:
        print("\033[32mFIM DO PROGRAMA. ATÉ LOGO!\033[m")
        print("==" * 30)
    return escolha

def validador(msg):
    while True:
        try:
            escolha = int(input(msg))
            if escolha not in [1, 2, 3]:
                raise ValueError
        except (ValueError, TypeError):
            print('\033[31mERRO! por favor digite uma alternativa correta!\033[m')
        except KeyboardInterrupt:
            print("\033[36mEntrada de dados interrompida pelo usuário!\033[m")
            return 3 
        else:
            return escolha


