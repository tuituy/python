def área(largura,comprimento):
    total = largura * comprimento
    print(f'A área de um terreno {largura}m X {comprimento}m é de {total}m².')


print('Controle de Terrenos')
print('-'*25)

largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
área(largura,comprimento)
