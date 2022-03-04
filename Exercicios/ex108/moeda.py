def metade(m=0):
    res = m / 2
    return res


def dobro(m=0):
    res = m * 2
    return res


def aumentar(m=0, c=0):
    taxa = c / 100
    res = m + (m * taxa)
    return res


def diminuir(m=0, c=0):
    taxa = c / 100
    res = m - (m * taxa)
    return res

def moed(funcao):
    return f'{funcao:.2f}'.replace('.', ',')
