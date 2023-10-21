def metade(n=0, formato=False):
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