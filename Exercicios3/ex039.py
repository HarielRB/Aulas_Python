from time import sleep
print('Impressão de números de 1 até 20')
c = 0
for c in range(1, 21):
    print('{} → '.format(c), end=' ')
    sleep(0.5)
print('FIM')