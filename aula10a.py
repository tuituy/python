n1 = float(input('Qual foi a sua primeira média?'))
n2 = float(input('Qual foi a sua segunda média?'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m >= 6.0:
    print('Nada além da sua obrigação!')
else:
    print('Sem videogame por 1 mês!!!')
#print('Parabéns' if m >= 6 else 'Estude mais!')
