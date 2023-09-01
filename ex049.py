n = int(input('Digite um número inteiro '))
print('Você escolheu a tabuada do {}'.format(n))
for c in range (1,11):
    r = n * c
    print('-='*7)
    print('{''} x {} = {}'.format(c,n,r))


    r = r+1
print('-='*7)
