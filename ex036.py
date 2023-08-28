valcasa = float(input('Qual é o valor da casa? '))
sal = float(input('Qual o seu salário? '))
anos = int(input('Em quantos anos você quer pagar? '))

prestação = valcasa / (anos * 12)
porcentagem = sal * 0.30

if prestação <= porcentagem:
    print('Você foi aprovado! a prestação fica em R$:{:.2f} por mês.'.format(prestação))
else:
    print('Você foi Reprovado, me desculpe.')
