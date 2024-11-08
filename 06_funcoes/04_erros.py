def dividir(num):
    try:
        divisao = num / 2

        if divisao == 0:
            print('Número não pode ser 0.')
        else:
            print(f'{num} / 2 = {num / 2}')
    except:
        print('Erro: número não pode  uma string')
    finally:
        print('Programa finalizado')

dividir(4)
dividir(0)
dividir(-4)
dividir('2')