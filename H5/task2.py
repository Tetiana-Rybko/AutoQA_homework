from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")

    wait = WebDriverWait(driver, 20)  # Увеличили время ожидания до 20 секунд

    try:
        first_photo = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gallery"]/li[1]')))
    except Exception as e:
        print("Ошибка при поиске первой фотографии:", e)
        driver.quit()
        return

    try:
        trash_area = wait.until(EC.visibility_of_element_located((By.ID, "trash")))
    except Exception as e:
        print("Ошибка при поиске корзины:", e)
        driver.quit()
        return


    actions = ActionChains(driver)
    actions.drag_and_drop(first_photo, trash_area).perform()

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="trash"]/ul/li')))

    trash_photos = driver.find_elements(By.XPATH, '//*[@id="trash"]/ul/li')
    assert len(trash_photos) == 1, f"Ожидалась 1 фотография в корзине, но найдено: {len(trash_photos)}"

    remaining_photos = driver.find_elements(By.XPATH, '//*[@id="gallery"]/li')
    assert len(remaining_photos) == 3, f"Ожидалось 3 фотографии в основной области, но найдено: {len(remaining_photos)}"

    print("Тест прошел успешно: фотография перемещена в корзину и оставшиеся фотографии на месте.")
    driver.quit()

test_drag_and_drop()