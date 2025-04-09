from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Указываем путь к драйверу (например, chromedriver)
driver = webdriver.Chrome(executable_path="path/to/chromedriver")
try:
 # Открываем сайт
 driver.get("https://www.google.com")
 # Находим поле поиска и вводим запрос
 search_box = driver.find_element(By.NAME, "q")
 search_box.send_keys("Selenium WebDriver")
 search_box.send_keys(Keys.RETURN)
 # Ждём и проверяем заголовок
 driver.implicitly_wait(10)
 print(driver.title)
finally:
 # Закрываем браузер
 driver.quit()