from ex109 import moeda
m = float(input('Insira o valor do produto: R$ '))
print(f'A metade do valor corresponde á {moeda.metade(m, p=False)}')
print(f'O dobro do calor corresponde á {moeda.dobro(m, True)}')
print(f'O acréssimo de 10% do valor corresponde á {moeda.aumentar(m, 10, True)}')
print(f'O desconto de 10% do valor corresponde á {moeda.diminuir(m, 10, True)}')
