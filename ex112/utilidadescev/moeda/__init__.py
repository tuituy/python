def metade(n=0, formato=False):
    '''
    Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.
    :param n: o preço que se quer reajustar.
    :param formato: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem o formato.
    '''
    resp = n / 2
    return resp if formato is False else moeda(resp)


def dobro(n=0, formato=False):
    resp = n * 2
    return resp if not formato else moeda(resp)


def aumentar(x=0, y=0, formato=False):
    porc = (x / 100) * y
    resp = x + porc
    return resp if formato is False else moeda(resp)


def diminuir(x=0, y=0, formato=False):
    porc = (x / 100) * y
    resp = x - porc
    return resp if formato is False else moeda(resp)


def moeda (preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')





def resumo(preço=0, taxaa=10,taxar=5 ):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço, True)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar, True)}')
    print('-'*30)












