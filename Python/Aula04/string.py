#Algumas propriedades String

nome = 'Denilson'

print(nome.upper())#Tudo Maiusculo
print(nome.lower())#Tudo minusculo
print(nome.title())#Primeira letra Maiuscula

texto = '  Olá Mundo!   '

print(texto)
print(texto.strip()) #Cortando os espaços
print(texto.lstrip())#Remove os espaços da esquerda
print(texto.rstrip())#Remove os espaços da direita

menu = 'Python'

print('####' + menu + '####')
print(menu.center(14))#Centralizar texto com tamanho de espaços 14
print(menu.center(14, '#'))#Centralizar com o cerquila nos espaços restante.

