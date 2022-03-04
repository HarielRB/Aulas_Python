print('TABUADA 4.0')
num = int(input('Informe o número da tabuada desejada: '))
inicio = int(input('Insira o valor inicail: '))
final = int(input('Insira o valor de término: '))
if final < inicio:
    while final < inicio:
        final = int(input('Insira o valor de termino: '))
for c in range(inicio, final + 1):
    print(f'{num} X {c} = {num * c}')
    c += 1
print('Tabuada construida com sucesso!!!!')
