larg = int(input('Quantos metros de largura tem a parede?'))
alt = int(input('uantos metros de Altura tem a parede?'))
area = larg * alt
tint = area / 2
print('A sua parede têm {} m² e você prescisará de um total de {} litros de tinta para pinta-la. '.format(area,tint))