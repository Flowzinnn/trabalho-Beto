
    
x = int(input('Digite o valor inicial: '))
y = int(input('Digite o valor final: '))

for i in range(x, y):
    
    for n in range(2, i):
        c = i % n
        if c == 0:
            continue
        
    print(f'O número {i} não é primo')