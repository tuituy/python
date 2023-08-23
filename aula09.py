frase = 'Curso em Video Python'
print(frase[9:14])# mostra do 9 ao 13

frase[9::3]#inicia no 9 até o fim mostrando 1 letra a cada 3 letras.
len(frase) #tamanho
frase.count('o')
frase.count('o',0,13)#procura o entre 0 e 13
frase.find('deo')#vai dar o inicio
frase.find('Android')# -1 significa n achou
'Curso' in frase #true ou false
frase.replace('Python','Android')#substituição
frase.upper()#maiusculo
frase.lower()#minusculo
frase.capitalize()#1 maiuscula
frase.title()#1 de cada palavra maiuscula
frase.strip()#remove final e inicio
frase.rstrip() #vai remover só os ultimos, r de right
frase.lstrip() #vai remover os espaços da esquerda, l de left
frase.split() #divide, retirando os espaços e começando a contagem denovo criando uma lista
'-'.join(frase)# junta tudo usando '-' para juntar
print(frase.upper().count('O')) #joga tudo para maiusculo e conta os O
print(len(frase.strip()))# vai contar quantos caracteres tem depois de retirar os espaços vazios do começo e final

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python','Android') # ele só vai trocar se colocar o 'frase =' antes

dividido = frase.split() # vai separar em uma lista de strings
print(dividido[0])# vai mostrar a primeira palavra da lista "Curso"
print(dividido [2] [3])# vai pegar a terceira palavra 'Vídeo' e vai pegar a 3 letra no caso 'e'


