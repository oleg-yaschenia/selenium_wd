from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://uat.erpvh.com/web/login"
link2 = "https://uat.erpvh.com/web?#action=210&active_id=1&model=account.invoice&view_type=list&menu_id=138"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_login = browser.find_element(By.ID, "login")
    input_login.send_keys("vitaly@ventor.tech")
    input_pass = browser.find_element(By.ID, "password")
    input_pass.send_keys("uatVive1234") #9MdBL9E7a6nY

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()
    browser.get(link2)

    time.sleep(5)
    button1 = browser.find_element(By.CSS_SELECTOR, ".o_search_options .o_dropdown  button")
    button1.click()
    time.sleep(1)
    button2 = browser.find_element(By.CSS_SELECTOR, "[data-id = '__filter__21']")
    button2.click()
    time.sleep(3)
    invoice = browser.find_element(By.CSS_SELECTOR, ".o_data_row")
    invoice.click()
    time.sleep(5)
    while True:
        time.sleep(2)
        sent_button = browser.find_element(By.CSS_SELECTOR, "[name='action_invoice_sent']")
        sent_button.click()
        time.sleep(8)
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "[name='info_form']")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        print(welcome_text, "- PASSED")
        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Preview as a PDF" == welcome_text
        time.sleep(2)
        close = browser.find_element(By.CSS_SELECTOR, "[type = 'button'].close")
        close.click()
        time.sleep(1)
        next_invoice = browser.find_element(By.CSS_SELECTOR, ".o_pager_next")
        next_invoice.click()


    # select = Select(browser.find_element(By.CSS_SELECTOR, ".position-static"))
    # select.select_by_value(x)  # ищем элемент с текстом "Python"

    # button = browser.find_element(By.CLASS, "[data-action-model='226']")
    # button.click()
    # time.sleep(5)
    # button = browser.find_element(By.CSS_SELECTOR, ".oe_kanban_color_11 [data-name='open_action']")
    # button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(100)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла


