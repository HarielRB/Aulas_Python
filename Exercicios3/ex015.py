print('Calculadora de tinta empresa X')
a = float(input('Informe a área da parede a ser pintada:'))
if a <= 54:
    print('Apenas uma lata de tinta é necessária')
    print('O valor a ser pago equivale a R$80.00')
else:
    L = a / 3
    la = L / 18
    print('Serão necessários {} litros de tinta'.format(L))
    print('Equivalente a {} latas de tinta'.format(la))
    print('O valor a ser pago é igual a R${:.2f}'.format(la * 80))
