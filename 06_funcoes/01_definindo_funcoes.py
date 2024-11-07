#Definindo uma função simples que soma dois números:
def soma(a,b):
    print(f'{a} + {b} = {a+b}')

soma(1,4)
print('-' * 20)

#Definindo uma função que multiplica dois números:
def multiplica(a,b):
    print(f'{a} * {b} = {a*b}')

multiplica(5,2)
multiplica(4,9)
multiplica(2,7)
multiplica(8,2)
print('-' * 20)

'''Tente criar uma função que calcule o preço total de um item com um desconto padrão de 5%. 
Assim, se o desconto não for informado, ele usa o valor padrão.'''

def valor_item(a, b=5):
    print(f'Valor do item: R${a}\nValor do desconto: {b}%.\nValor do item com desconto: R${a - ((a/100) * b)}')

valor_item(29.5)
valor_item(115, 8)
print('-' * 20)

#função co retorno

def soma(a,b):
    return a + b

print(soma(1,4))