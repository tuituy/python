parar = False
num = 1
print('-'*21)
while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*21)
    if num < 0:
        break
    for c in range (1,11):
        print(f'{num} x {c} = {c*num}')
    print('-'*21)



print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
