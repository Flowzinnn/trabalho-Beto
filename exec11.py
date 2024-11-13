#CONTADOR DE PALAVRAS UNICAS EM UMA FRASE:

frase = input('Digite uma frase: ')

frase_unica = frase.split(" ")

frase_unica = set(frase_unica)

print('O total de palavras únicas nesta frase é: ', len(frase_unica))