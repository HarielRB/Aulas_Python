from time import sleep
nome = str(input('Insira seu nome completo:')).strip().upper()
print('Irei procurar a Palavara RODRIGUES em seu nome, um momento...')
sleep(2)
if 'RODRIGUES' in nome:
    print('Sim, há RODRIGUES no seu nome.')
    print('Rodrigues aparece na posição: {}'.format(nome.find('RODRIGUES') + 1))
else:
    print('Não Há a palavra RODRIGUES em seu nome.')
