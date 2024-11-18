#(Calculadora Básica com Estruturas Condicionais) Peça ao usuário dois números e uma operação (adição, subtração, multiplicação ou divisão) e execute a operação escolhida.

def soma(x, y: int): # ao colocando def "função"(variavel: >int<): eu especifico que na função só pode ser recebido valores inteiros, apenas números
    return x + y

def subt(x, y: int):
    return x - y

def multp(x, y: int):
    return x * y

def div(x, y: int):
    return x / y

def operation(z: int):
    if z == 1:
        w = soma(x, y)
        print('O resultado da soma entre os dois valores fornecidos é:', w)
    
    elif z == 2:
        w = subt(x, y)
        print('O resultado da subtração entre os dois valores fornecidos é: ', w)
    
    elif z == 3:
        w = multp(x, y)
        print('O resultado da multiplicação entre os dois valores fornecidos é: ', w)
    
    elif z == 4:
        w = div(x, y)
        print('O resultado da subtração entre os dois valores fornecidos é: ', w)
    
    else: 
        print('Você nâo selecionou uma operação válida.')

x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
z = int(input('Digite a operação que deseja: 1 - para soma // 2 - para subtração // 3 - para multiplicação // 4 - para divisão.'))

operation(z)  
