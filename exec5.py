# GERADOR DE TABUADA PARA O NÚMERO SOLICITADO


# for i in range(1, 11):
#     tabuada = x * i
#     print(f'{x} x {i} = {tabuada}')
    
    
def criador_tabuada(x):
    for i in range(1, 11):
        tabuada = x * i
        print(f'{x} x {i} = {tabuada}')
    
x = int(input('Digite o número que deseja, que iremos criar uma tabuada dele: '))

criador_tabuada(x)