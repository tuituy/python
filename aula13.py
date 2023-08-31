

for c in range (0,6):
    print(c)
print('Fim')
-------------------------------------------------------
for c in range (6,0, -1):#o ultimo significa tirar ou colocar algo 2 vai pulando de 2 em 2
    print(c)
print('Fim')

for c in range (0,5):
    print('Arthur')
    if c == (2):
        print('Oi')
---------------------------------------------------------

n = int (input('Digite um número: '))
for c in range (0, n+1):
    print (c)
print('Fim')

---------------------------------------------------------
i = int(input('Inicio da contagem: '))
f = int(input('Fim da contagem: '))
p = int(input('Pula'))
for c in range (i, f+1, p):
    print(c)
print('Fim')

----------------------------------------------------------
s = 0
for c in range(0,3):
    n = int(input('Digite um valor: '))
    s = s+n
print('Fim, a soma foi {}'.format(s))