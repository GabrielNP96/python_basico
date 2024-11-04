#criando uma lista

numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)
print(type(numeros))

lista_numeros = [5, 10, 15, 20, 25]
print(lista_numeros)
lista_numeros[1] = 12
print(lista_numeros)

lista = []

for i in range(1,6):
    lista.append(i)

print(lista)
lista.remove(lista[2])
print(lista)

nova_lista = [1,2,3,4,5]
soma_nova_lista = 0
for i in nova_lista:
    soma_nova_lista += i

print(soma_nova_lista)

numeros_lista = [10, 20, 30, 40, 50]
print(len(numeros_lista))
print(sum(numeros_lista))
print(max(numeros_lista))
print(min(numeros_lista))