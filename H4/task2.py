import time
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # или убери, чтобы видеть браузер
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
def test_image_alt_attribute(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        # Ждём загрузки всех изображений (можно использовать WebDriverWait для надёжности)
    time.sleep(5)  # простой способ, лучше заменить на явное ожидание

        # Получаем все изображения
    images = driver.find_elements("tag name", "img")

        # Проверяем, что есть хотя бы 3 изображения
    assert len(images) >= 3, "Недостаточно изображений на странице"

        # Получаем атрибут alt у третьего изображения (индексация с 0)
    alt_text = images[2].get_attribute("alt")

        # Проверка значения alt
    assert alt_text == "award", f"Ожидалось 'award', но получено '{alt_text}'"