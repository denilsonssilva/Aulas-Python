#ESTRUTURAS CONDICIONAIS

maior_idade = 18
idade_especial = 17

idade = int(input('Informe sua idade: '))

if idade >= maior_idade:
    print('Pode tirar a Habilitação.')
else:
    print('Não tem idade para dirigir.')


#Utilizando o ELIF
if idade >= maior_idade:
    print('Pode tirar a Habilitação.')
elif idade == idade_especial:
    print('Poderá realizar as aulas teóricas, mas nao as aulas prática')
else:
    print('Não tem idade para dirigir.')

