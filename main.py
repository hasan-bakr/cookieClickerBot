from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(driver_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

bigCookie = driver.find_element(By.ID, 'cookie')
money = driver.find_element(By.ID, 'money')

buys = driver.find_elements(By.CLASS_NAME, 'grayed')
buy_moneys = []

timeout = time.time() + 2

while True:
    bigCookie.click()
    if time.time() > timeout:

        buys = driver.find_elements(By.CSS_SELECTOR, '#store b')
        buy_moneys = []

        for _ in buys:
            if _.text != "":
                buy_moneys.append(int(_.text.split("\n")[0].split(" - ")[1].replace(',', '')))

        buy_moneys.sort()

        for _ in buy_moneys:
            if _ > int(money.text):
                buys[buy_moneys.index(_) - 1].click()
                break
        timeout = time.time() + 2
