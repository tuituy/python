while True:
    try:
        int = int(input('Digite um número Inteiro: '))

    except:
        print('\033[0;31mERRO: por favor, digite um número inteiro válido.\033[m')
    try:
        real = float(input('Digite um número Real: '))
    except:
        print('\033[0;31mERRO: por favor, digite um número real válido.\033[m')
    else:
        print(f'O valor inteiro digitado foi {int} e o real foi {real}')
        break
