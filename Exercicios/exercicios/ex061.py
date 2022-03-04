from time import sleep
print('Gerador de PA com While')
termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razao: '))
c = 0
print('Calculando...')
sleep(1.5)
while c < 10:
    """Para fazer o exercicio sem a formula de PA basta criar uma variavel para o termo e outra para o contador
        t = termo
        logo após devemos ordenar que o programa print o termo dessa maneira 
            print('{}'.format(t))
        depois somamos o termo + razao para que ele receba a razao da PA
            t = t + razao"""
    ordem = c
    c = c + 1
    pa = termo + (razao * ordem)
    print(pa, end=' → ')
    sleep(0.5)
print('PA Apresentada com sucesso')
