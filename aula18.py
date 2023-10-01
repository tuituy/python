filme = {
    'titulo':'Star Wars','ano': 1977,'diretor':'George Lucas'}


print(filme.values())# os nomes dentro das keys
print(filme.keys()) # os nomes de cada valor
print(filme.items())# vai pegar os dois

for k,v in filme.items():# k é keys e v é o valor
    print(f'o {k} é {v}')







pessoas = {'nome':'Gustavo','sexo':'M','idade': 22}
#del pessoas['sexo']
pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5
print(pessoas['nome'])

for k, v in pessoas.items():
    print(f'{k} = {v}')


brasil = []
estado1 = {'uf':'Rio de Janeiro','sigla':'RJ'}
estado2 = {'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1.copy())
brasil.append(estado2)

print(brasil[0]['uf'])





estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())# funciona igual ao [:], que não funciona aqui o fatiamento
