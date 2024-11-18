#(Soma de Diagonais de uma Matriz Quadrada) Receba uma matriz quadrada de inteiros e calcule a soma dos elementos das diagonais principal e secundária.

matriz_p = [   
            
    [1, 3, 2, 7],
    [6, 4, 8, 9],
    [8, 3, 1, 5],
    [7, 6, 9, 8],
    
    ]

#print(len(matriz_p))
#print(matriz_p[3][4])

soma_diagonal1 = 0
soma_diagonal2 = 0
n = len(matriz_p)

for i in range(n):
    soma_diagonal1 += matriz_p[i][i]
    soma_diagonal2 += matriz_p[i][n - i - 1]
    #print(n - i - 1) = verificando se a matriz percore na direção contraria, resultado do print (3 - 2 - 1 - 0).

print('O resultado da soma da diagonal 1 é : ',soma_diagonal1)
print('O resultado da soma da diagonal 2 é : ',soma_diagonal2)