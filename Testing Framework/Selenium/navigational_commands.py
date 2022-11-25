from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.snapdeal.com/')
driver.get('https://www.amazon.in/')
driver.back()
driver.forward()
driver.refresh()
time.sleep(5)
driver.close()
