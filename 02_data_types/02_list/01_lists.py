#Listas são um dos 4 tipos de dados embutidos (built-in) em Python usados para armazenar coleções de dados

car_list = ['Uno', 'Palio','Celta', 'Gol']
print(car_list)

#acessando um item
print(car_list[0])
#trocando itens
car_list[2] = 'Fiorino'
print(car_list)
#descobrir tamanho da lista
print(len(car_list))
#adicionar item ao fim da lista
car_list.append('Celta')
print(car_list)
#para adicionar em um indice especifico:
car_list.insert(1, 'Civic')
print(car_list)
#unindo listas
car_list_two = ['Fox', 'Vectra','Siena','Fusca', 'Kombi']
car_list.extend(car_list_two)

print(car_list)
print(len(car_list))
#remover
car_list.remove('Vectra')
print(car_list)
#remover por indice
car_list.pop(7)
print(car_list)