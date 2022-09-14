from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
button = browser.find_element(By.ID, "book")
button.click()

x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = int(x_element.text)
y = calc(x)

input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)
browser.execute_script("window.scrollBy(0, 100);")  # Java Script


# Отправляем заполненную форму
button = browser.find_element(By.ID, "solve")
button.click()

