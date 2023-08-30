from datetime import date
ano = int(input('Qual é o seu ano de  nascimento? '))
atual = date.today().year
idade = atual - ano


if idade < 18:
    saldo = 18 - idade
    print('Você têm {} anos, vai se alistar em {} anos.'.format(idade,saldo))
    print('Seu alistamento será em {} ano.'.format(atual+saldo))
elif idade == 18:
    print('Você tem {} anos, está na hora de se Alistar!!'.format(idade))
else:
    saldo = idade - 18
    print('Você tem {} anos, já passou {} anos do alistamento.'.format(idade, saldo))
    print('Seu alistamento foi em {}.'.format(atual-saldo))




