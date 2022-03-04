nome = str(input('Insira seu nome: ')).strip().upper()
# cria-se uma variavel vazia
print(len(nome))
escada = ''
for c in range(len(nome), -1, -1):
    print(nome[:c])
print('-=-' * 20)
for c in range(0, len(nome)+ 1):
    print(nome[:c])
