def temaverde(msg):
    quantidade=len(msg)+4
    print(*quantidade)
    print(f"  {msg}")
    print('~'*quantidade)

def temaManual(txt):
    quantidade=len(txt)+4
    print("\033[01;46m~"*quantidade)
    print(f"  {txt}")
    print('~'*quantidade)


def ajuda(com):
    help(com)


c= ("\033[m"        #cor 0= cancelar
    "\033[32;40m"   #cor 1= vermelho

    
    
    )
    
### Conteudo principal ###
while True:
    mensagem=("SISTEMA DE AJUDA PyHELP")
    temaverde(mensagem)
    print('\033[m')
    texto=("Acessando o manual do comando ")
    comando=str(input("Function or library: "))
    temaManual(texto)
    print('\033[m')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)  
print("Até Logo!")   







