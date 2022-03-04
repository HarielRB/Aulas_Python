def metade(m=0, p=False):
    valor = m / 2
    return valor if p is True else moeda(valor)


def dobro(m=0, p=False):
    valor = m * 2
    return valor if p is True else moeda(valor)


def aumentar(m=0, c=0, p=False):
    valor = m + (m * (c / 100))
    return valor if p is True else moeda(valor)


def diminuir(m=0, c=1, p=False):
    valor = m - (m * (c / 100))
    return valor if p is True else moeda(valor)


def moeda(funcao):
    return f'R${funcao:.2f}'.replace('.', ',')


def resumo(m=0, taxaa=10, taxad=5):
    print('--' * 20)
    print(f'{"RESUMO DO VALOR":>25}')
    print('--' * 20)
    print(f'Preço Informado: \tR${m:.2f}')
    print(f'Metade do Valor:\t{metade(m, False)}')
    print(f'Dobro do Valor :\t{dobro(m)}')
    print(f'Aumento de {taxaa}%: \t{aumentar(m, taxaa)}')
    print(f'Desconto de {taxad} %: \t{diminuir(m, taxad)}')
