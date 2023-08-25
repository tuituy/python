nome = str(input('Qual é o seu nome? ')).strip()
if nome == 'Arthur':
    print('Que nome lindo você tem!')
else:
    print ('Não é o papai!')
    print('Bom dia, {}'.format(nome))