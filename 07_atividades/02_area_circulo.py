#Escreva um programa que calcule a área de um círculo, solicitando ao usuário o raio.
import math
def area_of_the_circle():
    try:
        radius = float(input('Digite o raio do circulo: '))
        area = math.pi * radius ** 2
        print(f'A área do círculo é {area:.2f}')
    except:
        print('Você precisa digitar um número valido')
    finally:
        print('Fim da aplicação')

area_of_the_circle()