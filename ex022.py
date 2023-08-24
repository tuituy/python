nome = str (input('Digite o Seu nome completo:')).strip()

print ('O seu nome com todas as letras maiúsculas é {}.'.format(nome.upper()))
print ('O seu nome com todas as letras minúsculas é {}.'.format(nome.lower()))

print('O texto todo sem considerar os espaços tem um total de {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem um total de {} letras'.format(nome.find(' ')))
separar = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separar[0], len(separar[0])))
