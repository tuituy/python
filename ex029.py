vel = int(input('Quantos Km/h você está rodando nessa estrada? km/h '))
if vel <= 80:
    print('Boa Viagem!!')
else:
    multa = (vel-80)* 7
    amais = vel-80
    print('Você está {}km/h acima do limite de velocidade, a multa é de R${:.2f}. '.format(amais,multa))
