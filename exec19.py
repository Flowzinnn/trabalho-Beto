# 19 (Contador de Caracteres de uma Frase) Receba uma frase e retorne um dicionário que contém a quantidade de cada caractere (inclusive espaços).

def frase_cont(x):
    dic = {}  #dicionario
    
    for i in x:
        dic[i] = x.count(i) #add quais sao os caracteres e define a quantidade de cada
    return dic
    
frase = input('Digite uma frase, iremos contar os caracteres: ')
caracter_cont = frase_cont(frase)
print('A quantidade de cada caracter é: ',caracter_cont)