def leiaint(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError,TypeError):
            print('ERRO!')
            continue
        else:
            return n


num=leiaint("Digite um numero inteiro: ")
print(f"O valor digitado foi: {num}")
