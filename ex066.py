num2 = 0
soma = 0
cont = 0
while True:
    num1 = int(input('Digite um valor (999 para parar): '))
    if num1 == 999:
        break
    soma = num1 + num2
    num2 = soma
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')

