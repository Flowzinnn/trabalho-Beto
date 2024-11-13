#Criar uma lista com a nota dos alunos -> fazer a media -> mostras as notas que ficarem apenas em cima da média

def criar_media(x):        # funcao para definir a media
    y = (sum(x)) / len(x)
    return y

list_notes = [8.0, 2.5, 4.6, 9.4, 10, 5.1, 6.7, 3.4, 8.9, 3.8, 1.5, 10, 7.5, 6.0] #essa foram as notas dos alunos

y = criar_media(list_notes)

print(f'A media dos alunos é de: {y}')

notasMaiorMedia = []
for i in list_notes:   
    if i >= y:
        notasMaiorMedia.append(i)
        
print(notasMaiorMedia)
