from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input_1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input_1.send_keys("Pet")
    input_2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input_2.send_keys("Lol")
    input_3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input_3.send_keys("test@test.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'text_file.txt')  # добавляем к этому пути имя файла
    load_file = browser.find_element(By.ID, "file")
    load_file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()