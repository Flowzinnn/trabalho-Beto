#Implementar um jogo de advinhação
#O usuario devera tentar chutes para advinhar o número de 1 a 100 que o computador escolher
#O programa deve retornar: 1 -> se o número escolhido pelo programa é maior ou menor do qual ele chutou
#2 - > O número de tentativas do jogador
from random import randint

def adv_game():
    attempts = 0
    num_sort = randint(1, 100)   
    while True:
        attempt = int(input('Tente advinhar o número que eu estou pensando: '))
        attempts += 1
        if attempt == num_sort:
            print(f'Parabéns, você acertou o número com um total de {attempts} tentativas!')
            return
        else:
            if attempt > num_sort:
                print('Você errou o número nessa tentativa, tente novamente com um valor menor!')
            elif attempt < num_sort:
                print('Você errou o número nessa tentativa, tente novamente com um valor maior!')    

adv_game()

#OBS: Notas para o professor: Sei que disse para usarmos funções que tenham apenas 1 responsabilidade, entretanto, acho que o senhor concordaria que -> 
#-> como um exercicio da lista que pede algo muito especifico, declarar apenas uma função que faça tudo é bem menos complicado do que declarar varias.