# CONVERSOR DE TEMPERATURA DE x PARA FAHRENHEIT

def conversor(x):
    y = (x * 1.8) + 32
    return y

x = float(input('Digite a temperatura atual em Graus Celsius para convertermos em Fahrenheit: '))

y = conversor(x)

print(f'A temperatura atual em Fahrenheit é de: {y}')



# def conversor(x):
#     x = (x * 1.8) + 32
    