try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:
    print('Erro encontrado      ;-;')
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado foi {r:.2f}')
finally:
    print('Até mais piá, volte sempre')
