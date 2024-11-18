#(Remoção de Elementos Duplicados) Receba uma lista de inteiros e retorne uma nova lista sem elementos duplicados, mantendo a ordem original.

def limparDup(listaInt):
    listaDup = list(dict.fromkeys(listaInt)) #função dict.fromkeys remove itens duplicado e a função dict preserva a ordem original
    return listaDup

lista_int = [1, 4, 2, 1, 5, 4, 7, 2, 7, 8, 1, 2, 4, 5, 3, 9, 10, 21, 12, 12, 15]
listaSemDup = limparDup(lista_int)
print(listaSemDup)
