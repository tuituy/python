def somar(a=0,b=0,c=0):
    '''
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: não retorna nada
    '''
    s = a + b + c
    return s
def funcao():

    n1 = 4
    print(f'N1 dentro vale {n1}')

somar(3,2,5)

n1 = 2
funcao()
print(f'N1 global vale {n1}')

r1 = somar(3,5,1)
r2 = somar(2,2)
r3 = somar(6)

print(f'Os resultados foram {r1} ,{r2} ,{r3}')
