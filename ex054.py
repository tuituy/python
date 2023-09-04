from datetime import date
atual = date.today().year
contadormenor = 0
contadormaior = 0
for c in range (1,8):

    ano = int(input('Qual ano a {}ª pessoa nasceu? '.format(c)))
    if atual - ano <= 21:
        contadormenor = contadormenor + 1

    else:
        contadormaior = contadormaior +1

print('{} são maiores de idade\nE {} são menores de idade.'.format(contadormaior,contadormenor))
