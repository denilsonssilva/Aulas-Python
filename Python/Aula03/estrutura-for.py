#Estrutura de repetição FOR

texto = input('Informe um texto: ')
vogais = 'AEIOU'

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end='')
else:
    print() # adiciona uma quebra de linha
