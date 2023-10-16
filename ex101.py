from datetime import date
data = date.today().year
print('-'*30)
def voto(idade):
    idade = data - ano
    return idade



ano = int(input('Em que ano você nasceu? '))
idade = voto(ano)
if idade < 16:
    obrigacao = ' NEGADO'
elif idade >= 16 and idade < 18:
    obrigacao = 'OPCIONAL'
elif idade >= 18 and idade < 65:
    obrigacao = 'OBRIGATÓRIO'
elif idade > 65:
    obrigacao = 'OPCIONAL'


print(f'Com {idade} anos: O VOTO É {obrigacao} ')
