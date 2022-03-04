print('Em que período você estuda?')
periodo = str(input('Insira M para matutino, V para vespertino ou N para noturno:')).strip().upper()
if periodo == 'M':
    print('Bom dia !')
elif periodo == 'V':
    print('Boa tarde!')
elif periodo == 'N':
    print('Boa noite!')
else:
    print('Período inválido')
