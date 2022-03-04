teste = []
teste.append('Hariel')
teste.append(21)
print(teste)
# há a necessidade da adição do elemento [:] para que a lista galera receba uma  'copia'
galera = []
galera.append(teste[:])
teste[0] = 'Karma'
teste[1] = 22
galera.append(teste[:])
print(galera)
