import playsound

print('Insira o número correspondente para o dia da semana')
print('1 --> Domingo')
print('2 --> Segunda')
print('3 --> Terça')
print('4 --> Quarta ')
print('5 --> Quinta ')
print('6 -->  Sexta ')
print('7 --> Sábado ')
num = int(input('Insira o número:'))
if num == 1:
    print('Domingo')
elif num == 2:
    print('Segunda')
elif num == 3:
    print('Terça')
elif num == 4:
    print('Quarta')
elif num == 5:
    print('Quinta')
elif num == 6:
    print('Sexta')
    playsound.playsound('teste2.mp3')
elif num == 7:
    print('Sábado')
    playsound.playsound('ex029.mp3')
else:
    print('Opção inválida!')
