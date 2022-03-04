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
    return f'{funcao:.2f}'.replace('.', ',')
