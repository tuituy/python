times = ('Botafogo','Palmeiras','Grêmio','Flamengo','Bragantino','Fluminense','Athletico-PR','Fortaleza','Atlético-MG','Cuiabá','Cruzeiro','Internacional','São Paulo','Corinthians','Bahia','Goiás','Santos','Vasco da Gama','América-MG','Coritiba')
print('-='*15)
print('Lista de times do Brasileirão: ',end=' ')
print(times)
print('-='*15)
print('Os 5 primeiros são ',end=' ')
print(times[:5])
print('-='*15)
print('Os 4 últimos são ',end=' ')
print(times[-4:])
print('-='*15)
print('Times em ordem alfabética: ',end=' ')
print(sorted(times))
print('-='*15)

for pos,times in enumerate(times):
    if times == 'Corinthians':
        print(f'O time {times} está na {pos+1} posição.')



