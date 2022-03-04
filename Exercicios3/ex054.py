print('---' * 20)
print('{:^40}'.format('ISHUZOKU BANK'))
print('---' * 20)
valor = int(input('Insira o valor de saque: R$ '))
cedula = 50
total_cedulas = 0
while True:
    if valor >= cedula:
        valor -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'{total_cedulas} cédulas de R${cedula} ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedulas = 0
        if valor == 0:
            break
print('---' * 20)
print('{:^40}'.format('ISHUZOKU BANK'))
print('{:^40}'.format('SEMPRE COM VOCÊ'))
print('{:^40}'.format('EM SEUS MELHORES MOMENTOS'))
print('---' * 20)
