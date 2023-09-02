homemvelho = ''
idadegeral = 0
idadegeralmedia= (idadegeral / 4)
idadehomemvelho = 0

idadem = 0

cont = 1


for c in range (1,5):
    n = str(input('Digite o {}º nome: '.format(c)))
    i = int(input('Digite a {}º idade:'.format(c)))
    sexo = int(input(''' Escolha o Sexo:
    [ 1 ] Masculino
    [ 2 ] Feminino
    '''))

    idadegeral = idadegeral + i
  
    if sexo == 2 and i < 20 :
        idadem = idadem + 1
    elif sexo == 1  and i > idadehomemvelho:
        homemvelho = (n)
        idadehomemvelho = (i)
    elif sexo < 1 or sexo > 2 :
        print('Código inválido')


print('A média de idade do grupo é {:.1f}, o nome do homem mais velho é o {} e existe {} mulheres com menos de 20 anos.'.format(idadegeral/4,homemvelho,idadem))



