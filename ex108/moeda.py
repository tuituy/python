def metade(n=0):
    resp = n / 2
    return resp


def dobro(n=0):
    resp = n * 2
    return resp


def aumentar(x=0, y=0):
    porc = (x / 100) * y
    resp = x + porc
    return resp


def diminuir(x=0, y=0):
    porc = (x / 100) * y
    resp = x - porc
    return resp

def moeda (preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.',',')