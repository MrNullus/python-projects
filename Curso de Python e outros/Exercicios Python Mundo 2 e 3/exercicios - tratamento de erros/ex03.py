import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print(" - Site Pudim está fora do ar :(")
else:
    print(" - Site Pudim ainda está no ar! :)")
    print(site.read())