cont = 1
maior = 0
menor = 0
for c in range (1,6):
    peso = float(input('Digite o {}º peso: '.format(cont)))
    cont = cont +1
    if c == 1:
        maior = peso
        menor = peso
    else:

        if peso > maior:
            maior = peso

        elif peso < menor:
            menor = peso





print('o maior peso foi o Kg {:.2f}\ne o menor foi Kg {:.2f}'.format(maior,menor))

