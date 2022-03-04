n = input('Digite seu nome completo:').strip()
s = n.split()
print('Seu primeiro nome é:{}'.format(s[0]))
print('Seu ultimo nome é:{}'.format(s[len(s)-1]))
print('Muito prazer em te conhecer {} {}!!!!'.format(s[0], s[-1]))
#O '[len(s)-1]' é utilizado pois o -1 contará o valor mais a direita da string
