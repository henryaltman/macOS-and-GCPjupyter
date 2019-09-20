from selenium import webdriver

browser = webdriver.Chrome()

def download_mp3(url,filename):
    with open(filename,'wb') as f:
        data = browser.get(url)
        f.write(data)


def download_img(url,filename):
    with open(filename,'wb') as f:
        f.write(url)


url = 'http://cdn-ali-us-w.dushu.io/audio/full/32aef7b21afc74c15c25bcd7501547f4_gqtrzr.mp3'

download_mp3(url,'复杂')