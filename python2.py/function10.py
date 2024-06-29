def temaverde(msg):
    quantidade=len(msg)+4
    print("\033[01;42m~"*quantidade)
    print(f"  {msg}")
    print('~'*quantidade)

def temaManual(txt):
    quantidade=len(txt)+4
    print("\033[01;46m~"*quantidade)
    print(f"  {txt}")
    print('~'*quantidade)

def linha():
    print("="*261)
def ajuda(com):
    help(com)

### Conteudo principal ###
while True:
    linha()
    mensagem=("SISTEMA DE AJUDA PyHELP")
    temaverde(mensagem)
    print('\033[m')
    texto=("Acessando o manual do comando ")
    linha()
    comando=str(input("Function or library: "))
    linha()
    temaManual(texto)
    print('\033[m')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)  
print("Até Logo!")   







