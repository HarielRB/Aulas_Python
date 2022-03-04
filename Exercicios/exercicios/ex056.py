from time import sleep
print('Analisador completo')
print('Primeiro iremos analisar a média das idades de vocês')
mi = 0
mulher = 0
# criar variavel para homem mais velho e sua idade idade
hvelho = 0
maior_idade = 0
for c in range(1, 5):
    nome = str(input('Insira o nome da {}ª pessoa: '.format(c))).strip().upper()
    idade = int(input('Insira a idade da {} ª pessoa: '.format(c)))
    sexo = str(input('Informe o  sexo da {} ª pessoa (F para feminino e M para masculino): '.format(c))).strip().upper()
    mi = mi + idade
    if sexo == 'F' and idade < 20:
        mulher = mulher + 1
    else:
        # criar condições para que o program identifique quem é o homem mais velho
        if c == 1:
            # como é o primeiro valor, não há comparativos, logo ele é o homem mais velho
            hvelho = nome
            maior_idade = idade
        if idade > maior_idade:
            # quando a idade for inserida e for maior que a variavel maior_idade, o programa irá substitui-la
            # juntamente com o nome
            hvelho = nome
            maior_idade = idade
media = mi / 4
print('ANALISANDO...')
sleep(3)
print('A média de idade entre vocês é {:.2f}.'.format(media))
if mulher != 0 and mulher != 1:
    print('Existem {} mulheres menores de 20 anos entre vocês'.format(mulher))
elif mulher == 1:
    print('Apenas uma mulher entre vocês é menor de 20 anos')
else:
    print('Nenhuma mulher entre vocês é menor de 20 anos')
print('O {} é o homem mais velho com {} anos'.format(hvelho, maior_idade))
