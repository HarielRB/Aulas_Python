print('Validação de datas')
data = input('Insira uma data (00/00/0000): ')
dia = int(data[0])
mes = int(data[3])
mes2 = int(data[4])
total = len(data)
if dia > 3:
    print('Data inválida')
elif mes > 1:
    print('Data inválida')
elif mes2 > 2:
    print('Data inválida')
elif total > 9 or total < 9:
    print('Data inválida')
else:
    print('Data aceita')