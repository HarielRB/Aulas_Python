lista_expressao = []
expressao = str(input('Digite a expressão: ')).strip()
lista_expressao.append(expressao)
contador_1 = 0
contador_2 = 0
for c in lista_expressao:
    print(c)
    for letra in c:
        if letra in '(':
            contador_1 += 1
        elif letra in ')':
            contador_2 += 1
contador_3 = contador_1 - contador_2
if contador_3 == 0:
    print('Expressão Valida')
else:
    print('\033[1;31m''Expressão inválida')
