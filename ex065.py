num1 = 0
cont = 1
num2 = 0
maior = 0
menor = 0
r = 'S'

while num1 != 'N' and r == 'S':
    num1 = int(input('Digite um número para calcular a média: '))
    media = (num1 + num2) / cont
    num2 = num2 + num1
    if cont == 1:
        maior = num1
        menor = num1
    elif num1 > maior:
        maior = num1
    elif num1 < menor:
        menor = num1
    print('''[{}] A soma dos números
[{}]Quantidade de números somados
[{}]Média 
[{}]Maior número digitado
[{}]Menor número digitado'''.format(num2,cont,media,maior,menor))
    cont += 1
    media = 0
    num1 = 0
    if num1 == 0:
        r = str(input('Deseja continuar? [S/N]').upper())





