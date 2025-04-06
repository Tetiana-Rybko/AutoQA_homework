import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://itcareerhub.de/ru")
driver.maximize_window()
time.sleep(1)


cookie_button = driver.find_element(By.XPATH, '//button[contains(text(),"Подтвердить")]')
cookie_button.click()

payment_button = driver.find_element(By.PARTIAL_LINK_TEXT, 'Способы оплаты')
payment_button.click()
time.sleep(1)

driver.save_screenshot('payment_screenshot.png')

time.sleep(2)
driver.quit()