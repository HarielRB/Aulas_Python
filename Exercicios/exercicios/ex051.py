from time import sleep
print('Demonstrador de Progessão Aritimética')
term = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão dessa PA: '))
print('CALCULANDO...')
sleep(3)
for c in range(0, 10):
    # poderia ser escrito dessa maneira:
    # criar uma variavel - ex decimo = term + (10 - 1) * razao
    # logo após escrever: for c in range(term, decimo + razao, razao)
    ordem = c
    pa = term + (razao * ordem)
    print(pa, end=' → ')
    sleep(1)
print('PA apresentada com sucesso')
