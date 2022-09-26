from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

WebDriverWait(browser, 20).until(EC.element_to_be_clickable(By.XPATH, "//type[@name='RESULT_RadioButton-7_0']")).click()