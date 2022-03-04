from uteis import numeros

num = int(input('Insira um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} corresponde á {fat}')
print(f'O dobro de {num} corresponde á {numeros.dobro(num)}')
