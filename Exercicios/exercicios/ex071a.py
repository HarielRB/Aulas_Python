# exercicio corrigido
print('BANCO X')
valor = int(input('DIGITE O VALOR PARA SAQUE: R$ '))
total = valor
cedulas = 50
total_cedulas = 0
while True:
    if total > cedulas:
        total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R$ {cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if total == 0:
            break
print('Volte sempre')
