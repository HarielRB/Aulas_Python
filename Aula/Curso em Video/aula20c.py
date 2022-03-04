# funções com lista
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f'O dobro dos valores de sua lista são: {lst}')


valores = [5, 7, 1, 0, 2, 3]
print(f'Essa é sua lista: {valores}')
dobra(valores)
