from time import sleep
nome = str(input('Insira seu nome:')).strip()
idade = int(input('Insira sua idade:'))
sexo = str(input('Escreva M para masculino ou F para feminino:')).upper()
print('Realizando cadastro....')
sleep(5)
if sexo == 'M':
    print('Nome:{} \n Idade:{}\n Sexo: Masculino'.format(nome, idade))
    print('Seus dados foram cadastrados, tenha um bom dia.')
elif sexo == 'F':
    print('Nome:{} \n Idade: \n Sexo: Feminino'.format(nome, idade))
else:
    print('Sexo Inválido')
