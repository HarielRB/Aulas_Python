galera = [['Hariel', 21], ['Karma', 33], ['Pedro', 21], ['João', 22]]
print(galera)
print(galera[0])
print(galera[0][0])
print(galera[2][1])
print(galera[3][0])
for p in galera:
    print(p)
print('Agora só os nomes')
for p in galera:
    print(p[0])
print('Agora o nome e idade')
for p in galera:
    print(f'Nome: {p[0]:^10} Idade: {p[1]:^10}')
