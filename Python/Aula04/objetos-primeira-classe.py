def somar(a, b):
    return a + b

def exibir_resultados(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')


exibir_resultados(10, 10, somar) # O resultado da operação 10 + 10 = 20

