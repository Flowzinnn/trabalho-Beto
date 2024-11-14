#Implementar um jogo de advinhação
#O usuario devera tentar chutes para advinhar o número de 1 a 100 que o computador escolher
#O programa deve retornar: 1 -> se o número escolhido pelo programa é maior ou menor do qual ele chutou
#2 - > O número de tentativas do jogador


def adv_game():
    from random import randint
    attempts = 0
    num_sort = randint(1, 100)
    
    while True:
        int(input('Tente advinhar o número que eu estou pensando: '))
    if attempt == num_sort:
        return('Parabéns, você acertou o número!')

adv_game()



# https://chatgpt.com/share/67355db3-d7dc-800a-a2dd-2e6ff96ee753