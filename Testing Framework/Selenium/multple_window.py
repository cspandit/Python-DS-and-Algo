# scenarios to handle multiple window in python

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('url')
x = driver.find_element(By.ID, 'id')
x.click()
windows = driver.window_handles
for x in windows:
    driver.switch_to.window(x)
    print(driver.title)