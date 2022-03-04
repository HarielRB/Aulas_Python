# Cores no Terminal
print('\033[1;31;43mOlá Mundo!\033[m')
# O \33[m no final encerra a configuração de texto
print('\033[7;30m Olá Hariel\033[m')

nome = 'Hariel'
print('Olá, muito prazer em te conhecer {}{}{} !!!'.format('\033[4;30m', nome, '\033[m'))
cores = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m', 'pretobranco' : '\033[7;30m'}

print('Olá {} {} {}'.format(cores['pretobranco'], nome, cores['limpa']))
