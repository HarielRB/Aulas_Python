v = float(input('Insira a velocidade do seu veículo atualmente?'))
if v>80:
    print('Você recebeu uma multa!')
    m = (v - 80)* 7
    print('O valor da multa é igual á é igual a R${:.2f}'.format(m))
    print('Diminua sua velocidade!!!')
else:
    print('Você está nos padrões de velocidade')
print('Tenha uma viagem segura!')
