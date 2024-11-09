#Crie um programa que peça ao usuário para digitar seu nome e imprima uma mensagem de boas-vindas.
def greetings():
    name = input('Digite seu nome: ')

    if not name:
        print('Por favor, digite seu nome. É necessário pelo menos um caractere.')
    else:
        print(f'Olá {name}! Bem vindo!')

greetings()