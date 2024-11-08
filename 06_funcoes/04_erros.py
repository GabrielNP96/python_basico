def dividir(num):
    try:
        if num == 0:
            print('Número não pode ser 0.')
        else:
            divisao = num / 2
            print(f'{num} / 2 = {divisao}')
    except TypeError:
        print('Erro: entrada inválida, o número não pode ser uma string ou um valor não numérico.')
    finally:
        print('Programa finalizado.')

# Testando a função
dividir(4)
dividir(0)
dividir(-4)
dividir('2')
