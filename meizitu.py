from bs4 import BeautifulSoup
import requests, re


class download_img(object):
    def __init__(self):
        self.url = "https://mzt.cx/"

    def startdown(self):
        resp = requests.get(self.url)
        html = BeautifulSoup(resp.text, 'html.parser')
        # print(html)
        with_imgs = html.find_all('div', class_="lazyload act2")
        for with_img in with_imgs:
            div = BeautifulSoup(str(with_img), "html.parser")
            img_url = re.findall(r'[^()]+', div.div['onclick'])[1].split(',')[0]



if __name__ == "__main__":
    img = download_img()
    img.startdown()
