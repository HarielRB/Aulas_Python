p = float(input('Insira o peso em quilos do peixe: KG'))
if p > 50:
    print('O peixe apresenta {} quilos a cima do valor permitido!'.format(p - 50))
    m = (p - 50) * 4
    print('Devido ao peso do peixe, você pagará uma multa no valor de: R${:.2f}'.format(m))
else:
    print('Não haverá multa!')
