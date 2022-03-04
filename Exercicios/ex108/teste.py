import ex108.moeda
m = float(input('Insira o valor do produto: R$ '))
print(f'A metade do valor corresponde á R${ex108.moeda.moed(ex108.moeda.metade(m))}')
print(f'O dobro do calor corresponde á R${ex108.moeda.moed(ex108.moeda.dobro(m))}')
print(f'O acréssimo de 10% do valor corresponde á R${ex108.moeda.moed(ex108.moeda.aumentar(m, 10))}')
print(f'O desconto de 10% do valor corresponde á R${ex108.moeda.moed(ex108.moeda.diminuir(m, 10))}')
