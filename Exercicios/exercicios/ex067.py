from time import sleep
print('TABUADA 3.0')
contador = 1
while True:
    num = int(input('Qual tabuada você deseja calcular ? '))
    print('-=-' * 20)
    if num < 0:
        print('ENCERRANDO PROCESSOS...')
        print('-=-' * 20)
        break
    else:
        for contador in range(1, 11):
            # para usar o while escreveriamos while contaro < 10:
            print(f'{num} X {contador} = {num * contador}')
    print('-=-' * 20)
sleep(2)
print('Até mais')
# Hariel lembrar que número negativo é menor que 0
