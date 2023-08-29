valor1 = int(input('Digite o Primeiro valor: '))
valor2 = int(input('Digite o Segundo valor: '))

if valor1 > valor2:
    print('O valor {} é maior que o valor {}.'.format(valor1,valor2))
elif valor2 >valor1:
    print('O valor {} é maior que o valor {}.'.format(valor2,valor1))
else:
    print('Não existe valor maior, os dois são iguais.')
