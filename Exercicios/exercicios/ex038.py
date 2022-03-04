from time import sleep
print('\033[1;35m''Comparador de números!!!''\033[m')
num_1 = int(input('Insira um número inteiro:'))
num_2 = int(input('Insira mais um número inteiro:'))
print('\033[35m''ANALISANDO...''\033[m')
sleep(2)
if num_1 > num_2:
    print('O primeiro valor é maior')
elif num_1 == num_2:
    print('Os valores são iguais.')
else:
    print('O segundo valor é maior.')
