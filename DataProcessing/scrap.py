import urllib.request
import urllib.parse
import json
import random
import os
from pywget import wget
import time

# documentation = https://unsplash.com/documentation


class Picture:
    def __init__(self, pic):
        self.unsplash_key = os.environ['UNSPLASH_KEY']    # add your unsplash key here
        request_headers = {
            "Authorization": f"Client-ID {self.unsplash_key}",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0"
        }
        self.pic = pic
        pageURL = f'https://api.unsplash.com/search/photos?page=4&per_page=100&query={self.pic}'
        request = urllib.request.Request(pageURL, headers=request_headers)
        self.contents = json.loads(urllib.request.urlopen(request).read())
        # print(json.dumps(self.contents, indent=4))
        self.results = self.contents['results']
        self.download_folder = 'MASK/download'

    def one_image(self):
        img = random.choice(self.results)
        return img['urls']['small']

    def user_one_image(self):
        load = self.one_image()
        self.download(load)
        print('downloaded')

    def many_image(self, amt):
        return [img['urls']['small'] for img in self.results[:amt]]

    def download(self, url):
        filename = wget.download(url, self.download_folder)
        os.rename(filename, filename+'.jpg')

    def user_many_image(self, amt):
        load_all = self.many_image(amt)
        for i in range(len(load_all)):
            try:
                self.download(load_all[i])
                print('> ', i)
                time.sleep(1)
            except Exception:
                print('x ', i, load_all[i])
                time.sleep(1)
        print('downloaded ', amt, 'images')


tik = Picture('man-covid-mask')
tik.user_many_image(19)