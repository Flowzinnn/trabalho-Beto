#(Calculadora de Fatorial Recursiva) Crie uma função recursiva que calcula o fatorial de um número dado pelo usuário.

def fatorial(num):
    if not isinstance(num, int) or num < 0: #o isinstance verifica se o numero digitado pelo usuário corresponde as expectativas, ou seja, a variavel num deve ser do tipo Int
        return None
    
    elif num == 0:
        return 1
    
    else:
        return num * fatorial(num - 1)

y = int(input('Digite o número a ser fatorado: ')) 
z = fatorial(y)
if z == None:
    print('ERRO: o número não pode ser negativo e também não pode ser quebrado. Ex: -4 // 6.3')
else:
    print(f'O número {y}, fatorado é igual a {z}')