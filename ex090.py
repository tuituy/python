aluno = {}
situação = 'Aprovado'
aluno['Nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["Nome"]}:' ))
print('-='*40)
print(f'- o nome é igual a {aluno["Nome"]}')
print(f'- média é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    print(f' - situação é igual a {situação}')
else:
    situação = 'Reprovado'
    print(f'- situação é igual a {situação}')
