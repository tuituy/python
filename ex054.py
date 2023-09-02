from datetime import date
atual = date.today().year
contadormenor = 0
contadormaior = 0
for c in range (0,7):

    ano = int(input('Qual ano você nasceu? '))
    if atual - ano <= 21:
        contadormenor = contadormenor + 1

    else:
        contadormaior = contadormaior +1

print('{} são maiores de idade e {} são menores de idade.'.format(contadormaior,contadormenor))
