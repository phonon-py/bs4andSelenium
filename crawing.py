from time import sleep, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


'''

selenium4系のためそのまま講義のコードは使用できない。具体的に言うと
find_element_by_nameのようなのは使用できなくなっている

'''

options = webdriver.ChromeOptions()
# 1.ヘッドレスモードでの使用
options.add_argument('--headless')
# 2.シークレットモードでの使用
options.add_argument('--incognito')
# 3.User-agentの設定
options.add_argument('--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36')

# step1 driverを作成する
driver = webdriver.Chrome(
    executable_path='/Users/kimuratoshiyuki/Dropbox/Python/hayatas-Udemy_スクレイピング/selenium/tools/chromedriver',
    options=options)
driver.implicitly_wait(10)

# step2 driver.get()でサイトにアクセスする
driver.get('https://atsumaru.jp/area/7/list?sagid=all')
sleep(2)

height = driver.execute_script("return document.body.scrollHeight")
new_height = 0

while True:
    print(height)
    # 1.スクロールする
    driver.execute_script(f'window.scrollTo(0, {height});')
    sleep(5)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if height == new_height:
        break

    height = new_height

sleep(3)

with open('company_list.html', 'w') as f:
    f.write(driver.page_source)

driver.quit()