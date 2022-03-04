def fatorial(num, show=False):
    """-->  Realiza o calculo fatorial do número especificado
    :parametro num: o número desejado para o calculo
    :parametro show: (opcional) é responsavel por mostrar ou não o processo
    return: o fatorial do número especificado em num"""
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
    return f


# programa principal
print(fatorial(5, show=True))
print(fatorial(4, show=True))
help(fatorial)
