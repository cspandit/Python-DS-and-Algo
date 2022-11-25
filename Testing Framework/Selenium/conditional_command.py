from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()
e = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print(e.is_enabled())
print(e.is_displayed())
e_radio = driver.find_element(By.XPATH, "//input[@id='gender-female']")
e_radio.click()
print(e_radio.is_selected()) # will return true


driver.quit()
