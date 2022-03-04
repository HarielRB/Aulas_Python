import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu Erro')
    print('O site não esta acessível no momento!')
else:
    print('tudo ok')
    print(site.read())
