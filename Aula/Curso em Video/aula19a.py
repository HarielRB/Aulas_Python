pessoas = {'nomes': 'Hariel', 'idade': 21, 'sexo': 'Masculino'}
print('Utilizando laços:')
for k in pessoas.keys():
    print(k)
print('Essas foram as chaves')
print('-' * 10)
for v in pessoas.values():
    print(v)
print('Esses foram os valores')
print('-' * 10)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('Esses foram os itens')
