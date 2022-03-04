import math
a = float(input("Informe o angulo para o calculo de seu sen, cos e tan:"))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O valor do seno corresponde a {:.2f},'
      ' \n O valor do cosseno equivale a {:.2f}'
      '\n O valor da tangente corresponde a {:.2f}'.format(s, c, t))
'''Lembre-se de converter os graus para radiano se nao da errado'''
