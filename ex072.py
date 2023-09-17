n = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
num = ' '
while num not in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20):
    num = int(input('Digite um número entre 0 e 20: '))
print(f'Você digitou o número {n[num]}')

