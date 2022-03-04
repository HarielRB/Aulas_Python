def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    opcao = 'NÃO VOTA'
    if idade == 16 or idade >= 65:
        opcao = 'VOTO OPCIONAL'
    elif idade >= 18:
        opcao = 'VOTO OBRIGATÓRIO'
    return f'Você tem {idade} e sua situação é {opcao}.'


i = int(input('Insira seu ano de nascimento: '))
print(voto(i))
