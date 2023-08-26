sal = float(input('Digite o salário do funcionário R$: '))
dez = (sal / 100) * 10
qui = (sal /100) * 15
if sal <= 1250:
    print('O aumento do funcionário é de 15% indo para R${:.2f}'.format(sal+qui))
if sal > 1250:
    print('O aumento do funcionário é de 10% indo para R${:.2f}'.format(sal+dez))
