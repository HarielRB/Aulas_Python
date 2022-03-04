import math
co = float(input('Digite o valor do cateto oposto:'))
ca = float(input('Digite o valor do cateto adjascente:'))
h = math.hypot(ca, co)
print('O valor da hipotenusa é igual a {:.2f}'.format(h))
