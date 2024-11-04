cidades = ['Contagem', 'Betim', 'Belo Horizonte', 'Juatuba']

for cidade in cidades:
    print(cidade)

print("-" * 15)

lista_de_frutas = ['Banana', 'Mamão', 'limão', 'Tomate']

for fruta in lista_de_frutas:
    print(fruta)

print("-" * 15)

for i in range(11):
    print(i)

print("-" * 15)

for i in range(0,101,10):
    print(i)

print("-" * 15)

soma = 0
for i in range(1,21,1):
    if i % 2 == 0:
        soma += i

print(soma) 

print("-" * 15)

soma_multiplos_de_tres = 0

for i in range(1,31,1):
    if i % 3 == 0:
        soma_multiplos_de_tres += i

print(soma_multiplos_de_tres)