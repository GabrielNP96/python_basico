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


soma = 0
for i in range(1,21,1):
    if i % 2 == 0:
        soma += i

print(soma) 
