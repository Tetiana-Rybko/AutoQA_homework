import pytest
from selenium import webdriver
from models import BasePage,LoginPage, InventoryPage,CartPage,CheckoutPage


def test_order_total():
    # Настройка драйвера
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    try:
        # Страница логина
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Страница инвентаря
        inventory_page = InventoryPage(driver)
        inventory_page.add_items_to_cart()

        # Переход в корзину
        inventory_page.go_to_cart()

        # Страница корзины
        cart_page = CartPage(driver)
        cart_page.proceed_to_checkout()

        # Страница оформления заказа
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_checkout_form("John", "Doe", "12345")

        # Получение итоговой стоимости
        total_price = checkout_page.get_total_price()

        # Проверка суммы
        assert total_price == "Total: $58.29", f"Ожидалась сумма $58.29, но получена {total_price}"

    finally:
        # Закрытие браузера
        driver.quit()