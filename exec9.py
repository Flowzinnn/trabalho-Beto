# VERIFICADOR DE MAIORIDADE

def verify_age(age):
    if age >= 18:
        print(f'Parabéns {name}, você já é maior de 18 e já pode ser preso!!')
    else:
        print(f'{name}, você ainda não completou 18 anos!!')

name = str(input('Digite seu nome: '))
age = int(input('Digite sua idade, vamos verificar se você já pode ser preso: '))

verify_age(age)

