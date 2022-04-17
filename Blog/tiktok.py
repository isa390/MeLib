from selenium import webdriver

# 路径是自己解压安装 Chromedriver 的路径
driver = webdriver.Chrome()

url = "http://itknow.tk"
url1 = "http://esabeila.gq"

driver.get(url)
driver.get(url1)