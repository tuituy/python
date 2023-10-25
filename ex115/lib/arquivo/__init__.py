from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # leitura de arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') # leitura de arquivo texto, se n tiver o + o cria.
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho ('PESSOAS CADASTRADAS')
        print(a.read())
