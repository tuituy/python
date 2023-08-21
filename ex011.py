larg = float(input('Quantos metros de largura tem a parede?'))
alt = float(input('uantos metros de Altura tem a parede?'))
area = larg * alt
tint = area / 2
print('A sua parede têm {:.2f} m² e você prescisará de um total de {:.2f} litros de tinta para pintá-la. '.format(area,tint))
