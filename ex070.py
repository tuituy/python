print('-'*40)
print('          LOJA SUPER BARATÃO        ')
print('-'*40)

total = 0
mais1000 = 0
nomebarato = ''
preçobarato = 0




while True:
    nome = str(input('Nome do Produto: '))
    preço = float(input('Preço R$: '))
    
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if total == 0:
        nomebarato = nome
        preçobarato = preço

    if preço < preçobarato:
        nomebarato = nome
        preçobarato = preço

    total = preço + total

    if preço > 1000:
        mais1000 += 1

    if continua in ('Nn'):
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi o/a {nomebarato} que custa R${preçobarato:.2f}')


