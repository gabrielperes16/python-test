import urllib
import urllib.request

try:
    site=urllib.request.urlopen('https://amafil.com.br/')
except  urllib.error.URLError:
    print("Deu erro")
else:
    print("Tudo certo")
    print(site.read())