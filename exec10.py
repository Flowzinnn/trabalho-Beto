#CALCULADORA DA ÁREA DE UM RETANGULO

def calc_areat(x, y):
    area = (x * y) / 2
    return area

print('Vamos calcular a área do retângulo!')

base = int(input('Digite o valor da base do triângulo:'))
altura = int(input('Digite a altura do triângulo: '))

area = calc_areat(base, altura)

print(f'A área do triângulo é = {area}cm²')

