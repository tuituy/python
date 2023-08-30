from datetime import date
ano = int(input('Qual o ano de nascimento do atleta? '))
atual = date.today().year
idade = atual - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9 :
    print('Categoria MIRIM.')
elif idade <= 14:
    print('Categoria INFANTIL.')
elif idade <=19:
    print('Categoria JUNIOR.')
elif idade <= 25:
    print('Categoria SÊNIOR')
elif idade >25:
    print('Categoria MASTER.')
