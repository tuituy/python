

nome = str(input('Qual é o seu nome? '))
if nome == 'Arthur':
    print('Que nome bonito!')
elif nome == 'Arthur' or nome == 'Geovana' or nome == 'Sergio':
    print('Nome bonito viu!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))
