# CONTAGEM DE NÚMEROS EM UMA LISTA

lista1 = [3, 12, 25, 36, 43, 54, 62, 71, 88, 95, 100]

print(f'A quantidade de números na lista 1 é: {len(lista1)}')

# DESAFIO EXTRA PRA MIM MESMO = Dessa vez, o usuário que ira colocar quantos números ele quer na lista

lista2 = []

while True:
    value = input('Digite um número para adicionar a lista, ou digite "fim" para terminar de colocar valores: ')
    
    if value.lower() == 'fim' :
        break
    
    try:
        number = int(value)
        lista2.append(number)
    
    except ValueError:
        print('Digite um número valido ou apenas "fim" para terminar.')
        
print(f'A quantidade de números na lista é {len(lista2)}')