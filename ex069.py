maioridade = 0
homens = 0
mulhermenor = 0

while True:
    print('_' * 25)
    print('   CADASTRE UMA PESSOA      ')
    print('_' * 25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).upper().strip()[0]
    resp = ' '

    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if idade > 18:
        maioridade += 1
    if sexo in 'mM':
        homens +=1
    if idade < 18 and sexo in 'Ff':
        mulhermenor +=1
    if resp in 'nN':
        break

print('======= FIM DO PROGRAMA =======')
print(f'Total de pessoas com mais de 18 anos: {maioridade}.')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulhermenor} mulheres com menos de 20 anos.')