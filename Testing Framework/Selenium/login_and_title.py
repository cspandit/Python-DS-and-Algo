from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


# If we don't want give executable_path, then place all drivers executables file in python installed location(Scripts)
# simply driver = webdriver.Chrome() will work
# driver = webdriver.Chrome(executable_path="C:\Drivers_for_sele\chromedriver_win32\chromedriver.exe")
# other way is using service object ser_obj = Service(executable_path) now it can be passed to Chrome class for
# initialization driver = webdriver.Chrome(service=ser_obj). service is mandatory this is not KWARGS

driver = webdriver.Chrome()
driver.get("https://m.facebook.com/")
driver.maximize_window()
x = driver.find_element(By.ID, 'm_login_email')
x.clear() # This will clear the remembered value
x.send_keys('cspandit123@gmail.com')
driver.find_element(By.ID, 'm_login_password').send_keys('@CHandu')
driver.find_element(By.NAME, 'login').click()
print(driver.title)
time.sleep(5)


