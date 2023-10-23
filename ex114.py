import urllib
import urllib.request


try:
    site = urllib.request.urlopen('http://www.google.com')
except urllib.error.URLError:
    print('O site Google não está acessível no momento.')
else:
    print('Consegui acessar o site Google com sucesso.')
    print(site.read())