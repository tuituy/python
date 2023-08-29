ano = int(input('Qual é o seu ano de  nascimento? '))

idade = 2022 - ano


if idade < 18:
    print('Você têm {} anos, vai se alistar em {} anos.'.format(idade,18-idade))
elif idade == 18:
    print('Você tem {} anos, está na hora de se Alistar!!'.format(idade))
else:
    print('Você tem {} anos, já passou {} anos do alistamento.'.format(idade, idade - 18))




