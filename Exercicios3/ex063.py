from datetime import date
hoje = date.today().year
taxa = 0.015
salario = float(input('Insira o valor do seu salário no início da contratação: R$'))
for c in range(1995, hoje + 1):
    print(f'Ano: {c}, Salário: R${salario:.2f}')
    c += 1
    if c == 1996:
        salario = salario + (salario * taxa)
    else:
        taxa_nova = 2 * taxa
        taxa = taxa_nova
        salario = salario + (salario * taxa)
print('Fim')
