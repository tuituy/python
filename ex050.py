soma = 0
cont = 0
 c in range (0,6):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 ==0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números pares e a soma foi {}.'.format(cont, soma))