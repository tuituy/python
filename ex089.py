lista = []
pessoa = []
media = []

resp = 'S'


while resp in 'S':

    nome = str(input('Nome: '))
    pessoa.append(nome)
    nota1 = float(input('Nota 1: '))
    pessoa.append(nota1)
    nota2 = float(input('Nota 2: '))
    pessoa.append(nota2)

    lista.append(pessoa[:])
    pessoa.clear()
    media.append((nota1+nota2) / 2)
    resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    if resp in 'N':
        break

print(lista)
print('-='*40)
print('Nº  NOME            MÉDIA')
print('-'*30)

for c in range (0,len(lista)):
    print(f'{c}    {lista[c][0]}',f'{media[c]:<20}')




