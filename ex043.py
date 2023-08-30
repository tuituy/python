peso = float(input('Digite seu peso (Kg) '))
altura = float(input('Digite sua altura (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f} '.format(imc),end= ''),
if imc < 18.5:
    print('você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('você está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('você está com sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('você está na obesidade!')
elif imc > 40:
    print('você está na obesidade mórbida!')
