# GERADOR DE TABUADA PARA O NÚMERO SOLICITADO

x = int(input('Digite o número que deseja, que iremos criar uma tabuada dele: '))

for i in range(1, 11):
    tabuada = x * i
    print(f'{x} x {i} = {tabuada}')
    