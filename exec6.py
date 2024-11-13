# CALCULADOR DE MÉDIA ARITMÉTICA

def criar_media(x1, x2, x3):
    media = (x1 + x2 + x3) / 3
    return media

n1 = float(input("Digite a nota da sua primeira prova: "))
n2 = float(input("Digite a nota da sua segunda prova: "))
n3 = float(input("Digite a nota da sua terceira prova: "))

media = criar_media(n1, n2, n3)

print(f'A média aritmética  das suas notas é: {media}')