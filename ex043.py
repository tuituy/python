peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Seu IMC é {:.2f}, você está abaixo do peso!'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é  {:.2f}, você está no peso ideal!'.format(imc))
elif imc >= 25 and imc < 30:
    print('Seu IMC é {:.2f}, você está com sobrepeso!'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.2f}, você está na obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é {:.2f}, você está na obesidade mórbida!'.format(imc))
