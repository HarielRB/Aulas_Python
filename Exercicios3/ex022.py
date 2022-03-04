from time import sleep
print('Sistema de aprovação escola pla plum')
nota_1 = float(input('Insira sua primeira Nota:'))
nota_2 = float(input('Insira sua segunda Nota:'))
print('Calculando...')
sleep(3)
media = (nota_1 + nota_2) / 2
if 10 > media >= 7:
    print('Parabéns, você foi aprovado')
elif media == 10:
    print('Aprovado com distinção')
else:
    print('Você reprovou')
    print('Estude mais no próximo ano')
