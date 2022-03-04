from datetime import date
print('Programa de Alistamento Militar')
ano = int(input('Informe os quatro digitos do ano de seu nascimento:'))
idade = date.today().year - ano
if idade < 18:
    print('Não há a necessidade de alistamento por enquanto.')
    rest = 18 - idade
    if rest == 1:
        print('Falta apenas um ano para você alistar-se. Fique atento.')
    else:
        print('Faltam {} anos para você se alistar.'.format(rest))
        print('O alistamento deverá ser feito em {}'.format(date.today().year + rest))
elif idade == 18:
    print('Você deve se alistar até novembro desse ano')
elif idade > 18:
    opcao = str(input('Você ja cumpriu o alistamento obrigatório?')).upper().strip()
    rest = idade - 18
    if opcao == 'SIM':
        print('Parabéns, você cumpriu suas obrigaçõpes como Brasileiro')
    elif opcao == 'NAO':
        print('\033[1;31m''Você deveria ter se alistado em {}''\033[m'.format(date.today().year - rest))
        print('\033[1;31m''Você está com um atraso de {} anos, Vá se alistar imediatamente.''\033[m'.format(rest))
else:
    print('Opção inválida.')
