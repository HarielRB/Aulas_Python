n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'A soma vale {s}')
# tecnica de f string
# para formatar casas depois da virgula basta escrever a variavel e o :.Xf
