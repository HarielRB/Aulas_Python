from time import sleep
print('\033[1;35m' 'DETETIVE PYTHON''\033[m')
print('Vou fazer algumas perguntas para você, Vamos lá')
while True:
    nome = str(input('Insira seu nome: ')).strip().upper()
    print('Responda as perguntas somente com sim ou nao')
    a = str(input('Você telefonou para a vítima? ')).strip().upper()
    b = str(input('Você esteve no local do crime? ')).strip().upper()
    c = str(input('Você mora perto da vítima ? ')).strip().upper()
    d = str(input('Você devia alguma quantia para a vítima? ')).strip().upper()
    e = str(input('Você trabalhou com a vítima? ')).strip().upper()
    colecao = [a, b, c, d, e]
    respostas = colecao.count('SIM')
    print('\033[1;35m''REUNINDO RESPOSTAS....''\033[m')
    sleep(3)
    if respostas == 2:
        culpa = '\033[1;36m''SUSPEITO''\033[m'
    elif 4 >= respostas >= 3:
        culpa = '\033[1;33m''CUMPLICE''\033[m'
    elif respostas == 5:
        culpa = '\033[1;31m''ASSASSINO''\033[m'
        print('Você está preso')
    else:
        culpa = '\033[1;32m''INOCENTE''\033[m'
    print('{} você é {}'.format(nome, culpa))
    opcao = str(input('Deseja continuar ? ')).strip().upper()
    if opcao == 'NAO':
        break
print('Até mais, foi muito bom jogar com você')
