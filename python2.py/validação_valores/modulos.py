def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print('\033[31mERRO! por favor digite um numero inteiro valido!\033[m')
            continue
        except(KeyboardInterrupt):
            print("\033[36mEntrada de dados interrompida pelo usuario!\033[m")
            continue
        else:
            return n

def leiafloat(msg):
    while True:
        try:
            n=float(input(msg))
        except (ValueError, TypeError):
            print("\033[m porfavor digite um numero inteiro!")
            continue
        except(KeyboardInterrupt):
            print("\033[m entrada de dados interrompida pelo usuario!")
            continue
        else:
            return n