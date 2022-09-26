import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



@pytest.mark.parametrize('link', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])
def test_answer(browser, link):
    try:
        browser.implicitly_wait(10)
        link = f"{link}"
        browser.get(link)
        answer = math.log(int(time.time()-28.5))
        input_data = browser.find_element(By.CSS_SELECTOR, "[placeholder='Напишите ваш ответ здесь...']")
        input_data.send_keys(f"{answer}")
        button_confirm = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        button_confirm.click()

        result = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        assert result == "Correct!", "Not Correct: " + result
    except:
        print("\n++++++++++++++" + result)

