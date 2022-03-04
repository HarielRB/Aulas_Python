"""from time import sleep
print('Demonstrador de PA')
termo = float(input('Insira o primeiro termo: '))
razao = float(input('Insira a razão da PA: '))
c = 0
print('Calculando....')
sleep(0.87)
while c < 10:
    ordem = c
    c = c + 1
    pa = termo + (razao * ordem)
    if c < 10:
        print(pa, end=' → ')
    else:
        print(pa, end=' ')
    sleep(0.5)
print(c)
termos_novos = int(input('Gostaria de mais quantos termos a mais? '))
d = 0
primeiro_termo = pa + razao
if termos_novos != 0:
    while d < termos_novos:
        ordem_nova = d
        d = d + 1
        pa_new = primeiro_termo + (razao * ordem_nova)
        if d < termos_novos:
            print(pa_new, end=' → ')
            sleep(0.5)
        else:
            print(pa_new, end=' ')
            sleep(0.5)
print('\nForam apresentados {} termos.'.format(c + d))
print('Até mais')"""
# o programa fez o que foi proposto apenas uma vez. para colocar a condição em laço, copiei o video
from time import sleep
print('Gerador de PA 3.0')
primeiro = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a Razão da PA: '))
c = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    # como o mais irá receber o número que o usuário irá inseri, ele será substituido, logo nao precisava da variavel ser classificada antes.
    total = total + mais
    while c <= total:
        print('{} →'.format(termo), end=' ')
        termo = termo + razao
        c = c + 1
        sleep(0.5)
    print('PAUSA')
    mais = int(input('Você gostraria de mais quantos termos ? '))
print('Foram apresentados {} termos ao total'.format(c - 1))
print('FIM')