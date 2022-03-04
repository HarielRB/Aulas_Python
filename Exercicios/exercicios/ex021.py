'''Feito com ajuda da video aula'''
n = input('Oi, qual é o seu nome ?')
import playsound
print('Olá, {}'.format(n))
print('Hoje irei escolher uma musica  para você {}, espero que goste'.format(n))
input('Vamos lá?')
playsound.playsound('ex021.mp3')
print(emoji.emojize('Espero que tenha gostado :blush: :heart:', use_aliases=True))
