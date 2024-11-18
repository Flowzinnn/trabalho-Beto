#(Contagem de Vogais e Consoantes) Peça ao usuário uma frase e conte o número de vogais e consoantes. Ignore espaços e caracteres especiais.

def verifVC(frase):
    vogais = "aeiouAEIOU"
    
    totalVogal = sum(frase.count(v) for v in vogais)
    totalConsoante = sum(1 for c in frase if c.isalpha() and c not in vogais)     # c.isalpha verifica se o valor é um caracter
    
    return totalVogal, totalConsoante

frase = input('Digite uma frase: ')
vogal, consoante = verifVC(frase)
print(f'A frase tem um total de: {vogal} vogais e de: {consoante} consoantes.')
    