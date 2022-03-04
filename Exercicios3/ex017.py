from time import sleep
print('Tempo estimado de download')
tamanho_arquivo = float(input('Insira o tamanho do arquivo em Mbs:'))
velocidade = float(input('Insira a velocidade em Mbps:'))
print('CALCULANDO...')
sleep(3)
horas = tamanho_arquivo // velocidade
resto = tamanho_arquivo % velocidade
if resto > 0:
    print('Seu arquivo levará {} horas e {:.0f} minutos para download'.format(horas, resto))
elif horas == 1:
    print('Seu arquivo levará {} hora para download'.format(horas))
else:
    print('Seu arquivo levará {} horas para o download'.format(horas))
