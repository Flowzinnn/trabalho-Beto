# VERIFICADOR DE NÚMEROS IMPARES E PARES
def verif(x):
    if x % 2 == 0:
        print('O número é par.')
    else:
        print('O número é impar.')

x = int(input('Digite um número: '))
verif(x)



