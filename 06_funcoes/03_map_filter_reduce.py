from functools import reduce
numeros = [1,2,3,4,5,6,7,8,9,10]

#map
numeros_dobrados = list(map(lambda x : x * 2, numeros))

print(numeros_dobrados)

#filter
numeros_par = list(filter(lambda x : x % 2 == 0, numeros))
print(numeros_par)

#reduce
produto = reduce(lambda x,y: x *y, numeros_par)
print(produto)

