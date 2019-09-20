# 爬取 iting 的 mp3，图片，用于机器学习 (收藏的)


# 思路一
# 需要模拟登陆，cookie 设置
# 需要先找到图片页，在图片页有 mp3实际链接、文本（原文）、插图


import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import urllib

iting_login_url = 'https://iting.club/login.html'
browser = webdriver.Chrome()
browser.get(iting_login_url)


# 模拟登陆功能，然后跳转到收藏
def login(user,passwd):

    account_input= browser.find_element_by_id('mobile')
    account_input.send_keys(user)

    passwd_input= browser.find_element_by_id('passwordInput')
    passwd_input.send_keys(passwd)

    login_button = browser.find_element_by_id('login-btn')
    login_button.click()

    browser.implicitly_wait(5)
    # time.sleep(1)
    print(browser.get_cookies())

# 登陆成功后跳转到收藏
def to_favorite():
    # 等待页面加载成功再进一步操作
    # wait = WebDriverWait(browser, 10)
    # wait.until(browser.find_element_by_id('login-btn'))
    # time.sleep(5)   # 最好用 wait 方法 实现
    browser.implicitly_wait(10)
    my_favorite = browser.find_element_by_id('footer_paid')
    my_favorite.click()


# 选择器（根据 class，取出提取的收藏项目，返回的节点都是 wedelement 对象）

def get_favorite_list():
    # time.sleep(3)   # 最好用 wait 方法 实现
    browser.implicitly_wait(10)
    my_favorite_list = browser.find_elements_by_css_selector('.speeches')
    print(my_favorite_list)
    # print(my_favorite_list)
    for favorite in my_favorite_list:
        favorite_ = favorite.find_elements_by_css_selector('*')
        for class_ in favorite_:
            if class_.get_attribute('href') != None:
                class_link = class_.get_attribute('href')
                print(class_link)
                browser.get(class_link)
                mp3list = browser.find_elements_by_class_name('icon.icon-introduction')
                for m in mp3list:

                    browser.get(m.get_attribute('href'))
                    img_url = browser.find_elements_by_css_selector('.main img[src]')
                    img_name = browser.find_elements_by_css_selector('head title')
                    print(img_url, img_name)
                    # download_img(img_url, img_name)

# 定义打开一个页面内指定类型节点的方法
def open_by_class(class_name):
    return browser.find_elements_by_class_name(class_name)


def download_mp3(url,filename):
    with open(filename,'wb') as f:
        f.write(url)


def download_img(url,filename):
    with open(filename,'wb') as f:
        f.write(url)




if __name__ == '__main__':

    login('13229038230','qwer1234')
    to_favorite()
    get_favorite_list()


# 思路二
# 模拟浏览器登陆后请求获得 https://iting.club/content/xxx(数字).html 所有地址

#
# if __name__ == '__main__':
#
#
#     login('13229038230','qwer1234')
#