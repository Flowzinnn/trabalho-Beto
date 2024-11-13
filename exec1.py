# CALCULADORA DE SOMA SIMPLES
def soma(x, y):
    return x + y

print('Bem vindo a calculadora de soma.')
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))

z = soma(x, y)

print(f'A soma dos números é de: {z}')