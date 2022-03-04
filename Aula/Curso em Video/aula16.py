lanche = ('hamburguer', 'Suco', 'Pizza', 'Pudim')
# tuplas podem ser criadas sem parenteses
# tuplas são imutaveis
print(lanche)
print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[:2])
# testando imutabilidade
# lanche[1] = 'Refrigerante'
# print(lanche[1])
for c in lanche:
   print(f'Eu vou comer {c}')
   # para identificar a posição devemos enumerar a tupla e criar uma variavel a mais no for
   # for pos, comida in enumerate(lanche)
    # print(f'Eu vou comer {comida} na posição {pos}')
# for cont in range(0, len(lanche)):
   # print(lanche[cont])
   # essa maneira permite apresentar a posição
print('Comi demais!')
# ambos os fors possuem o mesmo resultado, ele deve ser adequado ao programas
