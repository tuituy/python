ano = int(input('Qual o ano de nascimento do atleta? '))
idade = 2023 - ano

if idade <= 9 :
    print('Categoria MIRIM.')
elif idade <= 14 and idade > 9:
    print('Categoria INFANTIL.')
elif idade <=19 and idade > 14:
    print('Categoria JUNIOR.')
elif idade == 20:
    print('Categoria SÊNIOR')
else:
    print('Categoria MASTER.')
