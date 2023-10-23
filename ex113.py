def leiaInt(n):
    while True:
        try:
            a = int(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mERRO. Por favor digite um número Inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return a


def leiafloat(n):
    while True:
        try:
            a = float(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mERRO. Por favor digite um número Real válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return a


inteiro = leiaInt('Digite um número Inteiro: ')
real = leiafloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')
