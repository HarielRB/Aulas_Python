c = str(input('Insira o nome da sua cidade:'))
s = c.upper()
a = s.strip()
print('O nome da sua cidade é: {}'.format(a))
n = a.split()
print('Sua cidade começa com a palavra Santo?')
if 'SANTO' in n[0]:
    print('Sim, sua cidade começa com a palavra SANTO')
else:
    print('Sua Cidade não começa com a palavra SANTO')

'''poderia ser colocado o .strip na frente da variavel c
não era necessário usar o split, poderia colocar print(cid[:5].upper == 'SANTO') '''
