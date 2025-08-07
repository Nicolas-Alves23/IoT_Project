import urllib.request

url = 'https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_fullbody.xml'
urllib.request.urlretrieve(url, 'haarcascade_fullbody.xml')

print("Arquivo baixado com sucesso!")