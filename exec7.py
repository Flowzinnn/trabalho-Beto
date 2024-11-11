# INVERSOR DE STRING

pn = str(input('Digite uma palavra, iremos inverter ela: '))

pi = "" # Palavra Invertida: variavel para receber as letras e inverter a palavra

for i in range(len(pn)):
    pi = pn[i] + pi
     
print(pi)