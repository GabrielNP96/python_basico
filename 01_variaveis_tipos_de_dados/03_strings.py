#Python oferece métodos nativos para manipulação de strings.
#acessar partes da string.
minha_str = "Minas Gerais"
print(minha_str[0:5]) #pega os indices informados.

print(minha_str.upper())#tudo em maiúsculo.
print(minha_str.lower())#tudo em minúsculo.
frase = 'Sou de Minas.'
frase = frase.replace('Minas', 'Minas Gerais')#Faz substituições.
print(frase)