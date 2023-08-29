nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média é {}, você está reprovado!!'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média é {}, você está de recuperação!!'.format(media))
elif media >= 7.0 and media <= 10:
    print('Sua média é {}, você foi aprovado!!'.format(media))
