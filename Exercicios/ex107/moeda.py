def metade(m):
    res = m / 2
    return res


def dobro(m):
    res = m * 2
    return res


def aumentar(m, c=1):
    taxa = c / 100
    res = m + (m * taxa)
    return res


def diminuir(m, c=1):
    taxa = c / 100
    res = m - (m * taxa)
    return res
