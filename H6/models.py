from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def click(self, by, value):
        element = self.wait_for_element(by, value)
        element.click()

    def send_keys(self, by, value, text):
        element = self.wait_for_element(by, value)
        element.send_keys(text)

    def get_text(self, by, value):
        element = self.wait_for_element(by, value)
        return element.text

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        self.send_keys(*self.USERNAME_INPUT, username)
        self.send_keys(*self.PASSWORD_INPUT, password)
        self.click(*self.LOGIN_BUTTON)

class InventoryPage(BasePage):
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    TSHIRT_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_ICON = (By.XPATH, '//*[@class="shopping_cart_link"]')

    def add_items_to_cart(self):
        self.click(*self.BACKPACK_ADD_BUTTON)
        self.click(*self.TSHIRT_ADD_BUTTON)
        self.click(*self.ONESIE_ADD_BUTTON)

    def go_to_cart(self):
        self.click(*self.CART_ICON)

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.XPATH, '//*[@data-test="checkout"]')

    def proceed_to_checkout(self):
        self.click(*self.CHECKOUT_BUTTON)

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.XPATH, '//*[@data-test="continue"]')
    TOTAL_PRICE_LABEL = (By.XPATH, '//*[@class="summary_total_label"]')

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.send_keys(*self.FIRST_NAME_INPUT, first_name)
        self.send_keys(*self.LAST_NAME_INPUT, last_name)
        self.send_keys(*self.POSTAL_CODE_INPUT, postal_code)
        self.click(*self.CONTINUE_BUTTON)

    def get_total_price(self):
        return self.get_text(*self.TOTAL_PRICE_LABEL)

