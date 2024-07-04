try:
    a= int(input("Digite um valor:"))
    b=int(input('Digite um valor:' ))
    r=a/b
except (ValueError, TypeError):
    print(f"pErro de dados!")
else:
    print("Deu certo!")
finally:
    print("Volte sempre!")