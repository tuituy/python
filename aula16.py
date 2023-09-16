#TUPLAS SÃO IMUTÁVEIS, da erro
lanche = ('Hambúrguer','Suco','Pizza','Pudim')#TUPLAS
print(lanche[-2])
print(lanche[1:3])# desconsidera o ultimo
print(lanche[:2])# do início até o elemento 2/ desconsiderando o elemento 2
for comida in lanche:
    print(f'Eu vou comer {comida}')
print(len(comida))# tamanho da Tupla
