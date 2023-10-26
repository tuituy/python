from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resp = menu(['Ver pessoas cadastradas','Cadastrar Pessoas','Sair do Sistema'])
    if resp == 1:
        # opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)


    elif resp == 2:
        cabeçalho1('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resp == 3:
        cabeçalho1('Saindo do sistema... Até logo!')
        sleep(2)
        break
    else:
        print('ERRO! Digite uma opção válida')
        sleep(1)