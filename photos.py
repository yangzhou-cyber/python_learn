import requests
from bs4 import BeautifulSoup
from contextlib import closing

resp = requests.get('https://unsplash.com/s/photos/flower')

html = BeautifulSoup(resp.text, 'html.parser')
imgs = html.find_all('img')
num = 0
for img in imgs:
    num = num + 1
    src = BeautifulSoup(str(img), "html.parser").img['src']
    imgBuffer = requests.get(src, stream=True)
    with closing(imgBuffer) as r:
        with open('%d.jpg' % num, 'ab+') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
