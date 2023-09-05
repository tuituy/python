sexo = ''

cont = 1
while sexo != 'F' or sexo != 'M' and cont != 0:
    sexo = str(input('Qual é o Seu Sexo? [F/M]: ')).upper()
    if sexo == 'F':
        print('Muito obrigado, você é uma mulher!')
        cont = 0
    elif sexo == 'M':
        print('Muito obrigado, você é um homem!')
        cont = 0
print('Fim')
