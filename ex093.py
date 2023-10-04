jogador = {}
jogador['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
total = 0

for c in range(1,partidas+1):
    gols1 = int(input(f'Quantos golda na partida {c}? '))
    gols.append(gols1)
    total += gols1
jogador['gols'] = gols
jogador['total'] = total
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas}.')
for c in range(0,partidas):
    print(f'     => Na partida {c}, fez {jogador["gols"][c]} gols. ')
print(f'Foi um total de {jogador["total"]} gols.')
