pessoas = {'nomes': 'Hariel', 'idade': 21, 'sexo': 'Masculino'}
print('Utilizando o comando del')
print(f'antes do comando: {pessoas} ')
del pessoas['sexo']
print(f'Depois do comando del excluindo o indice sexo: {pessoas}')
