#criando um dicionario
produto = {
    'nome' : 'Bala',
    'preco' : 0.10,
    'estoque' : 200 
}
print(produto)
print('-' * 15)

produto['estoque'] -= 10
print(produto['estoque'])
print('-' * 15)

del produto['preco']
print(produto)
print('-' * 15)

print('estoque' in produto)