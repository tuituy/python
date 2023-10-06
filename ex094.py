galera = []
pessoa = {}
continua = 'S'
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('Erro!, Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continua in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if continua == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f}')
print('As mulheres cadastradas foram ',end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]}',end='')
print()
print('Lista das pessoas que estão acima da média:')
for p in galera:
    if p['idade'] >= media:
        print(f'\n{p["nome"]} com {p["idade"]}',end='')
        print()
