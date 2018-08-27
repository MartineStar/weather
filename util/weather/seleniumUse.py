import time
from selenium import webdriver


# 浏览器自启动打开
def start_browser(url):
    time.sleep(3)
    browser = webdriver.Chrome(executable_path = r'chromedriver.exe')
    browser.get(url)
    browser.implicitly_wait(5)
    browser.maximize_window()
    return browser

def aduio_browser(city):
    browser = webdriver.Chrome(executable_path = r'chromedriver.exe')
    browser.get('http://www.weather.com.cn/')
    browser.implicitly_wait(5)
    browser.maximize_window()
    itxt = browser.find_element_by_id('txtZip')
    itxt.send_keys(city)
    button = browser.find_element_by_id('btnZip')
    button.click()
    time.sleep(20)
    browser.close()

if __name__ == '__main__':
    aduio_browser('广州')