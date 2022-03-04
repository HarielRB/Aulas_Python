def area(comp, larg):
    a = comp * larg
    print(f'O terreno com proporções de {comp} X {larg} possui uma área de {a:.2f}')


print('Calculadora de aréa de terrenos')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(comprimento, largura)
