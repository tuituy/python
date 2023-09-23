valor = []
maior = 0
menor = 0
posicaomaior = []
posicaomenor = []

for c in range(0,5):
    valor.append(int(input(f'Digite um valor para a posição {c}: ')))



print(f'Você digitou os valores {valor}')

if len(valor) == 5 :
    maior = valor[0]
    menor = valor[0]

for c,i in enumerate(valor):
    if valor[c] > maior:
        maior = valor[c]
        posicaomaior.append(c)
        print(posicaomaior)
        print(f'O maior valor é {maior} e está nas posições {posicaomaior}')







print(maior)
