from datetime import date
pessoa = {}
data = date.today()

anosaposentar = 35 -  data.year

nome = str(input('Nome: '))
pessoa['nome'] = nome
ano = int(input('Ano de nascimento: '))
pessoa['idade'] = data.year - ano
idade = (data.year - ano)
carteira = int(input('Carteira de Trabalho (0 se não tiver): '))
pessoa['ctps'] = carteira
if carteira != 0:
    contratação = int(input('Ano de Contratação: '))
    pessoa['contatação'] = contratação
    salario = float(input('Salário: '))
    pessoa['salario'] = salario
    pessoa['aposentadoria'] = 35 - (data.year - contratação) + idade

print(pessoa)
for k,v in pessoa.items():
    print(f' {k} tem o valor de {v} ')


