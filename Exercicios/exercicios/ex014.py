c = float(input('Qual a temperatura em °C:'))
f = (c * 9/5) + 32
k = c + 273.15
print('A conversão de {}°C equivale a {:.2f}°F ou {:.2f}K'.format(c, f, k))
