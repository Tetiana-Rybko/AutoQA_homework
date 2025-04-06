from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://itcareerhub.de/ru")
    yield driver
    driver.quit()

def test_logo(driver):
    logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tn-elem__7178437221710153310155"))
    )
    assert logo, "Логотип не найден"

def test_programs(driver):
    programs_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Программы'))
    )
    assert programs_link, "Ссылка 'Программы' не найдена"

def test_payment(driver):
    payment_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Способы оплаты'))
    )
    assert payment_link, "Ссылка 'Способы оплаты' не найдена"

def test_news(driver):
    news_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Новости'))
    )
    assert news_link, "Ссылка 'Новости' не найдена"

def test_about_us(driver):
    about_us_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'О нас'))
    )
    assert about_us_link, "Ссылка 'О нас' не найдена"

def test_reviews(driver):
    reviews_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'Отзывы'))
    )
    assert reviews_link, "Ссылка 'Отзывы' не найдена"

def test_language_switch(driver):
    de_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'de'))
    )
    ru_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, 'ru'))
    )
    assert de_link, "Ссылка 'de' не найдена"
    assert ru_link, "Ссылка 'ru' не найдена"

def test_call_icon(driver):
    call_icon = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tel__7178437221710153310161"))
    )
    assert call_icon, "Иконка трубки не найдена"

    call_icon.click()
    message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"]'))
    )
    assert message, "Сообщение 'Если вы не дозвонились...' не найдено"
