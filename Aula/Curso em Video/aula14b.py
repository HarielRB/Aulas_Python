# sempre que o limite não for definido, utilize o while
r = 'S'
while r == 'S':
    n = int(input('Insira um número: '))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
print('FIM')