print('Identificador de centenas, dezenas e unidades')
numero = int(input('Insira um número inteiro de 0 até 999: '))
# primeiro: encntrar o valor das centenas por meio de uma divisão inteira
centenas = numero // 100
# segunto: encontrar o valor das dezenas por meio do resto da divsão do numero por 100
dezenas = numero % 100
# terceiro: encontrar o valor das dezenas por meio de uma divisão inteira por 10
quantidade_dezenas = dezenas // 10
# quarto: repetir os passos para a unidade
unidades = dezenas % 10
if centenas == 0 and quantidade_dezenas == 0:
    print('UNIDADES: {}'.format(unidades))
elif centenas == 0:
    print('DEZENAS: {}'.format(quantidade_dezenas))
    print('UNIDADES: {}'.format(unidades))
else:
    print('CENTENAS: {}'.format(centenas))
    print('DEZENAS: {}'.format(quantidade_dezenas))
    print('UNIDADES: {}'.format(unidades))
