print('DEMONSTRADOR DE FATORIAIS')
multiplicar = 1
num = 0
c = 0
while num != 'SAIR':
    num = input('Insira um número entre 1 e 16 [SAIR para sair]: ').strip().upper()
    if num != 'SAIR':
        print('{} ! = '.format(int(num)), end=' ')
        for c in range(int(num), 0, -1):
            print('{}'.format(c), end=' ')
            if c > 1:
                print('X ', end='')
            else:
                print('= ', end='')
            multiplicar *= c
        print(multiplicar)
print('FIM')
