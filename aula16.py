#TUPLAS SÃO IMUTÁVEIS, da erro
lanche = ('Hambúrguer','Suco','Pizza','Pudim')#TUPLAS
print(lanche[-2])
print(lanche[1:3])# desconsidera o ultimo
print(lanche[:2])# do início até o elemento 2/ desconsiderando o elemento 2
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer {comida}na posição {pos}')
print(len(comida))# tamanho da Tupla

for cont in range(0,len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print(sorted(lanche))# mostra em ordem alfabética


a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)
print(len(c))
print(c.count(5))#conta quantas vezes aparece o numero 5
print(c.index(8))# vai mostrar qual a posição está o número 8
del(a)# apaga a tupla, ou qualquer coisa
