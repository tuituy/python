cont = 1
maior = 0
menor = 0
for c in range (0,5):
    peso = float(input('Digite o {}º peso: '.format(cont)))
    cont = cont +1

    if peso > maior:
        maior = peso

    elif peso < maior:
        menor = peso




print('o maior peso foi o Kg {:.2f} e o menor foi Kg {:.2f}'.format(maior,menor))

