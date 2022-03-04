def contador(*num):
    tamanho = len(num)
    print(f'Você me passou {tamanho} números')


contador(1, 5, 3, 7, 9)
contador(0, 1, 2)
contador(0)
