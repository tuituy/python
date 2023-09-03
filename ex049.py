n = int(input('Digite um número inteiro '))
print('Você escolheu a tabuada do {}.'.format(n))
for c in range (1,11):

    print('-='*6)
    print('{} x {} = {}'.format(c,n,n*c))

print('-='*6)
