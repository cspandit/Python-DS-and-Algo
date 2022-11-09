# Test case to login using locator x path and check title of the page

from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/')
time.sleep(2)
x = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
x.send_keys('Admin')
time.sleep(2)
x = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')
x.send_keys('admin123')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(2)
title_actual = driver.title
assert title_actual == 'OrangeHRM'
