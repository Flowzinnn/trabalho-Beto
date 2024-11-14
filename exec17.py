# (Ordenação de Lista com Números Negativos e Positivos) Dada uma lista de números inteiros que incluem positivos e negativos, 
# ordene-os de forma que os negativos fiquem antes dos positivos, mantendo a ordem original relativa entre eles.

lista_pn = [-5, 2, 3, 4.5, -6, -2, -7, 12, 3, -4, -1, 0, 9.1, 8, 15, 13, 6]
lista_ordenada_n = []
lista_ordenada_p = []

for i in lista_pn:
    if i < 0:
        lista_ordenada_n.append(i)
    elif i > 0:
        lista_ordenada_p.append(i)

lista_pn = lista_ordenada_n + lista_ordenada_p
print(lista_pn)