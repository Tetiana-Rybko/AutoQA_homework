from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_text_in_iframe(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    found = False

    for i, iframe in enumerate(iframes):
        driver.switch_to.frame(iframe)
        try:
            body_text = driver.find_element(By.TAG_NAME, "body").text
            print(f"\n---- Текст внутри iframe {i} ----\n{body_text}\n")
            if "semper posuere integer et senectus justo curabitur" in body_text.lower():
                found = True
                break
        except Exception as e:
            print(f"Ошибка при чтении текста в iframe {i}: {e}")
        finally:
            driver.switch_to.default_content()

    assert found, "Искомый текст не найден ни в одном iframe"