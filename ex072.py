n = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete',
     'Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze',
     'Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
continua = 'S'
while continua == 'S':
    num = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {n[num]}')
    continua = (str(input('Você quer continuar? [S/N]'))).upper().strip()[0]

    if continua != 'S':
        break



