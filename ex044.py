valor = float(input('Qual o valor do produto? R$'))
print('-=-'*20)
opção = int(input('''[1] Dinheiro/cheque , à vista.
[2] No cartão, à vista.
[3] 2 x no cartão.
[4] 3x ou mais, no cartão.
Digite a condição de pagamento:'''))
print('-=-'*20)

if opção == 1 :
    print('Você recebeu um desconto de 10%, o valor vai ser de R$:{}'.format(valor-(valor*0.10)))
elif opção == 2:
    print('Você recebeu um desconto de 5%, o valor vai ser de R$:{}'.format(valor-(valor*0.05)))
elif opção == 3:
    print('O valor vai ser de duas parcelas de R$:{}'.format(valor/2))
elif opção == 4:

    parcelas = int(input('Quantas parcelas? '))
    juros = valor * 0.20
    pagar = (valor + juros) / parcelas

    if parcelas < 3:
        print('Opção Inválida.')

    else :
        print('Então serão {} parcelas de R$:{:.2f}'.format(parcelas,pagar))
print('-=-'*20)
