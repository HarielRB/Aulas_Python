f = str(input('Digite uma frase:')).strip().upper()
print('Vou te dar algumas informações sobre ela:')
print('Número de letras A presentes na frase:{}'.format(f.count('A')))
print('Ela aparece pela primeira vez na posição: {}'.format(f.find('A')+1))
print('Ela aparece pela ultima vez na posição: {}'.format(f.rfind('A')+1))
#O '+1' ali é pra somar á posição, pois o python conta o primeiro caractere como 0