parentes = []
expressao = str(input('Digite a expressão: '))


for i, v in enumerate(expressao):
    if v in '(':
        parentes.append('('[0])
    elif v in ')':
        if len(parentes) > 0:
            parentes.pop()
        else:
            parentes.append(')')
            break
if len(parentes) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
print(parentes)







