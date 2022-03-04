lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# sorted organiza a ordem de apresentação
print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
# o comando + esta juntando as duas tuplas na ordem que foram inseridas
print(c)
print(len(c))
print(c.count(5))
print(c.index(8))
# index = em que posição esta o caractere
print(c.index(5, 2)) # identificando o caractere a partir da 2 posição
for pos, cont in enumerate(c):
    if cont == 5:
        print(pos, end=' ')