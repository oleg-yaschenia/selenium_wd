from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)


    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

