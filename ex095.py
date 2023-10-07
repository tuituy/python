jogadores = []
jogador = {}
while True:
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    gols = []
    total = 0

    for c in range(1,partidas+1):
        gols1 = int(input(f'Quantos gols na partida {c}? '))
        gols.append(gols1)
        total += gols1
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())

    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'cod nome             gols           total')
print('-'*40)
for c in range(0,len(jogadores)):
    print(f'{c} {jogadores[c]["nome"]}             {jogadores [c]["gols"]}     {jogadores[c]["total"]}')
print()
print('-'*40)
while True:
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        print('Volte Sempre')
        break
    print(F'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]["nome"]}')

    for c in range(0,len(jogadores[dados]['gols'])):
        print(f' No jogo {c+1} fez {jogadores[dados]["gols"][c]}')

