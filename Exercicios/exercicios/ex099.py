from time import sleep


def maior(*tupla):
    tamanho = len(tupla)
    pos = 0
    ma = 0
    while pos < len(tupla):
        sleep(0.5)
        print(tupla[pos], end=' ')
        if pos == 0:
            ma = tupla[pos]
        elif tupla[pos] > ma:
            ma = tupla[pos]
        pos += 1
    sleep(0.5)
    print(f'Foram informados {tamanho} valores ao todo.')
    sleep(0.5)
    print(f'O Maior valor informado foi {ma} ')


maior(0, 3, 5, 2)
print('~~' * 40)
maior(3, 5, 7, 9, 100)
print('~~' * 40)
maior(6)
print('~~' * 40)
maior()
print('~~' * 40)
maior(6, 6, 6, 6)
