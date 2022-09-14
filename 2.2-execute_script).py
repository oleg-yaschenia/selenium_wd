from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = int(x_element.text)
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    browser.execute_script("window.scrollBy(0, 100);") #Java Script
    checkbox1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox1.click()


    radio1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

