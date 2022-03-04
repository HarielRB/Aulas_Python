print('Igualador de populações')
# problema de crescimento populacional
# igualara as populações ou ultrapassar
a = 80000  # população inicial A
taxa_a = 0.03  # taxa de crescimento populacional A
b = 200000  # populaçõa inicial B
taxa_b = 0.015  # taxa de crescimento populacinao B
anos = 0  # contador de anos
while a < b:
    a = a + (a * taxa_a)
    b = b + (b * taxa_b)
    anos = anos + 1
print('Serão necessários {} anos para que as populações sejam iguais'.format(anos))
