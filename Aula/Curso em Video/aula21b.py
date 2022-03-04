def par(num):
    if num % 2 == 0:
        return True
    else:
        return False


# programa principal
n = int(input('Insira um número: '))
if par(n):
    print('O número é par')
else:
    print('O número é impar')
