#Dicionários são usados ​​para armazenar valores de dados em pares chave:valor.

my_dog = {
    'nome': 'preta',
    'raca': 'vira-lata',
    'cor': 'preta'
}

print(my_dog)

#decobrindo número de itens
print(len(my_dog))
#acessando um valor
print(my_dog['cor'])
#descobrindo todas as chaves
print(my_dog.keys())
#criando um novo par chave : valor
my_dog['pelo'] = 'liso'
print(my_dog)
#obtendo todos os valores
print(my_dog.values())
#obtendo todos os itens
print(my_dog.items())
#iterando
for x, y in my_dog.items():
    print(x + ' : ' + y)