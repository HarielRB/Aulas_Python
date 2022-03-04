nome = str(input('Qual é o seu nome? ')).strip().upper()
if nome == 'HARIEL':
    print('Olá Mestre, como vai ?')
elif nome == 'HARIANNE':
    print('Olá Sînhá, como vai ?')
else:
    print('Olá {}, como vai você?'.format(nome))
