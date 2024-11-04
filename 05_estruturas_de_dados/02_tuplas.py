#criando uma tupla
tupla = (1,2,3,4,5)
print(type(tupla))
print(tupla)

print('-' * 15)

print(tupla[0])
print(tupla[4])

print('-' * 15)

nova_tupla = (10,20,30)
a,b,c = nova_tupla
print(f'{a}\n{b}\n{c}')

print('-' * 15)

print(5 in tupla)

print('-' * 15)

print(tupla + nova_tupla)