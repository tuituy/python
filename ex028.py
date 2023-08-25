from random import choice
lista = [0,1,2,3,4,5]
num = choice(lista)

escolha = int(input('Sorteei um número inteiro entre 0 e 5, vamos ver se você adivinha:'))
if escolha == num:
    print('Vc só deu sorte!, mas acertou.')
else:
    print('Hahaha, errou o número era {}.'.format(num))

