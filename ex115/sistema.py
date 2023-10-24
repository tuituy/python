from ex115.lib.interface import *
from time import sleep


while True:
    resp = menu(['Criar Arquivo','Cadastrar Pessoas','Sair do Sistema'])
    if resp == 1:
        cabeçalho1('Opção 1')
        clear_screen()

    elif resp == 2:
        cabeçalho1('Opção 2')
        clear_screen()
    elif resp == 3:
        cabeçalho1('Saindo do sistema... Até logo!')
        sleep(2)
        break
    else:
        print('ERRO! Digite uma opção válida')
        sleep(1)