frase = 'Curso em video python'
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('python', 'Android'))
print('Curso' in frase)
print(frase.find('Curso'))
print(frase.lower().find('curso'))
print(frase.split())

'''Para testos ongos utilizamos aspas 3 vezes, exemplo a baixo'''
print('''O menino quer um burrinho
para passear.
Um burrinho manso,
que não corra nem pule,
mas que saiba conversar.''')