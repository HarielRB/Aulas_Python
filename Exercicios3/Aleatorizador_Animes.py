from random import choice
from time import sleep
lista = []
anime = {}
while True:
    anime['Nome'] = str(input('Digite o nome do anime: ')).strip()
    anime['Episodios'] = int(input('Digite o número de episódios do anime: '))
    lista.append(anime.copy())
    while True:
        continuar = str(input('Deseja continuar ? [S/N] ')).strip().upper()
        if continuar in 'SN':
            break
        else:
            print('\033[1;31m''Opção inválida''\033[m')
    if continuar == 'N':
        break
print('-=-' * 20)
print('Sorteando anime....')
print('-=-' * 20)
sleep(2)
escolha = choice(lista)
print(f'O anime escolhido foi {escolha["Nome"]} e ele tem {escolha["Episodios"]} episódios no total.')
