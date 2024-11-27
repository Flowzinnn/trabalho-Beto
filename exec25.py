def filtroPar(lista):
    return [x for x in lista if x % 2 == 0]
   
listaNum = []

while True:
    number = input('Digite um numero ou digite "sair" para cancelar: ')
    
    if number == 'sair':
        break 
    
    try:
        number = int(number)
        listaNum.append(number)
    
    except ValueError:
        print('Digite um numero valido ou apenas sair para terminar')

listaPar = []
listaPar = filtroPar(listaNum)
print('Os números pares são: ',listaPar)




#atualizando a lista fazendo alguns exercicios que não precisam ser contados caso vale nota, estou fazendo após a data de entrega e estou apenas salvando no mesmo repositorio.
