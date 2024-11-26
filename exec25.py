def filtroPar(x):
    if x % 2 == 0:
        return x
   
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

print(listaNum)
listaPar = []
for i in range(len(listaNum)):
    listaPar = filtroPar(listaNum)
print(listaPar)