def ajuda(funcao):
    help(funcao)


print('~' * 30)
print('PyHelp')
print('~' * 30)
while True:
    aju = str(input('\033[1;34m''Digite a Função ou biblioteca desejada: ''\033[m')).strip()
    if aju.lower() == 'fim':
        break
    else:
        ajuda(aju)
