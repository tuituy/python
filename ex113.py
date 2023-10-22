def leiaInt(n):
    while True:
        try:
            a = int(input('Digite um número Inteiro: '))
            return a
        except:
            print('\033[0;31mERRO. Por favor digite um número Inteiro válido\033[m')
        else:
            break


def leiafloat(n):
    while True:
        try:
            a = float(input('Digite um número Real: '))
            return a
        except:
            print('\033[0;31mERRO. Por favor digite um número Real válido\033[m')
        else:
            break


inteiro = leiaInt('Digite um número Inteiro: ')
real = leiafloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')
