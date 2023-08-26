km = int(input('Digite a distância da viagem, Km '))
menor = km * 0.50
maior = km * 0.45
if km <= 200:
    print('O valor a se pagar por essa viagem é de R$:{:.2f}'.format(menor))
else:
    print('O valor a se pagar por essa viagem é de R$:{:.2f}'.format(maior))
