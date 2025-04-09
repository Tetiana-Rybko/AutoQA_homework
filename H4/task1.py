from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("http://uitestingplayground.com/textinput")
    yield driver
    driver.quit()

def test_button_text_change(driver):
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.clear()
    input_field.send_keys("ITCH")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    updated_button = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "ITCH")
    )
    assert updated_button, "Текст кнопки не изменился на 'ITCH'"