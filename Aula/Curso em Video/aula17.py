# num = (2, 5, 9, 1)
from typing import List
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
print(f'Lista em ordem crescente: {num}')
num.sort(reverse=True)
print(f'Lista em ordem decrescente: {num}')
num.insert(2, 0)
print(f' Utilizando o insert: {num}')
# num.pop()
# print(f'Utilizando o pop sem index: {num}')
num.pop(2)
print(f'Utilizando o pop com index: {num}')
num.insert(2, 2)
print(num)
num.remove(2)
# o comando remove irá remover o primeiro número 2 que aparecer na lista
# para fazer com que ele remova todos será necessário um laço
print(num)
