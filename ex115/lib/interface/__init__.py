def leiaInt(msg):
    while True:
        try:
            a = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!. Por favor digite um número Inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return a


def linha(tam = 42):
    return '-' * tam

def clear_screen():
    for c in range (100):
        print('')



def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def cabeçalho1(txt):
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c +=1
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc

