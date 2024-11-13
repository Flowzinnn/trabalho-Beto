#Números Primos em um Intervalo

def verificar_primo(num):
    if num <= 1: #numeros iguais a 1 ou menores não são primos
        return False
    for i in range(2, int(num ** 0.5) + 1): #verifica até a raiz do numero
        if num % i == 0:
            return False # se for divisivel por qualquer número, não é primo
    return True # se não encontrar nenhum divisor, é primo

x = int(input('Digite o primeiro valor entre o intervalo: '))       #Pega o primeiro valor do intervalo
y = int(input('Digite o valor final do intervalo: '))               #Pega o ultimo valor do intervalo

lista_primos = []                      #Cria uma lista para adicionar os números primo
for i in range(x, y + 1):              #For para verificar os primos entre os intervalos(Y recebe + 1 para não terminar antes de verificar o último numero)
    if verificar_primo(i):    #chama a função para verificar se é primo no momento i
        lista_primos.append(i)   # adicionar o número(caso seja primo, na lista_primos)
print(f'Os números primos entre o valor {x} e o valor {y} são: {lista_primos}')     

