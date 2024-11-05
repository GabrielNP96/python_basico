#definindo conjutos
conjunto_1 = {1,2,3,4,5,6}
conjunto_2 = {5,6,7,8,9,10}
print(conjunto_1)
print(conjunto_2)
print('-' * 20)

#união dos conjuntos
conjunto_união = conjunto_1 | conjunto_2
print(conjunto_união)
print('-' * 20)

#interseção
conjuto_intersecao = conjunto_1 & conjunto_2
print(conjuto_intersecao)
print('-' * 20)

#diferença
conjuto_diferenca = conjunto_1 - conjunto_2
print(conjuto_diferenca)
print('-' * 20)

#diferença simétrica
conjunto_diferença_simétrica = conjunto_1 ^conjunto_2
print(conjunto_diferença_simétrica)
print('-' * 20)
