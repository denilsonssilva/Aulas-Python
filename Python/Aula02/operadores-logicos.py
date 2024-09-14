#Operadores Lógicos

#Na condição AND para ser TRUE, tudo deve ser TRUE.
#Na condição OR para ser TRUE, apenas um precisa ser TRUE.

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)

saldo = 1000
saque = 300
limite = 100
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque

print(exp)

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

print(exp_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite 
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(exp_3)


#Mais exemplos com NOT
contatos_emergencia = []

not 1000 > 1500

not contatos_emergencia

not 'saque 1500'

not ''

