nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5.0:
    print('Sua média é {:.1f}, você está reprovado!!'.format(media))
elif 6.9 >= media >= 5.0 :
    print('Sua média é {:.1f}, você está de recuperação!!'.format(media))
elif 10 >= media >= 7.0 :
    print('Sua média é {:.1f}, você foi aprovado!!'.format(media))
