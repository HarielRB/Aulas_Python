nome = input('Qual é o seu nome ?')
print('Prazer em te conhecer {:^20}!'.format(nome))
n1 = int(input('Insira um valor {}:'.format(nome)))
n2 = int(input('Agora mais um meu consagrado:'))
print('A soma vale {} \n A multiplicação vale {} \n A divisao é {:.2f} \n e a subtração é igual a {} '.format(n1+n2, n1*n2, n1/n2, n1-n2))
print('A divisão inteira é {} e o resto é {}'.format(n1//n2, n1%n2))
print('E por fim, a exponenciação é: {}'.format(n1**n2))

