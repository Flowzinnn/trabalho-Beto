#Verificador de PALINDROMOS(Palavras que se leem igualmente de frente para tras e de tras para frente)
# Puxar a palavras -> verificar se ela é um palindromo -> Se sim, retornar (A palavra é um palindromo)

def verif_palindromo(x):
    y = ""
    for i in range(len(x)):
        y = x[i] + y
    if y == x: 
        return print('A palavra é um Palindromo')
    else: 
        return print('A palavra não é um Palindromo')
    
pn = str(input('Digite a palavra, vamos verificar se ela é um palindromo(se lê igual de trás para frente): '))
verif_palindromo(pn)
