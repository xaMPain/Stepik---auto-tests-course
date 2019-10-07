from selenium import webdriver
import time

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector('input[type="text"]')
    # напечатать в поле текста в каждом элементе
    for element in elements:
        element.send_keys("Мой ответ")
    button = browser.find_element_by_css_selector("button.btn").click()
    # переключиться на всплывающее окно
    alert = browser.switch_to.alert
    # вывести последний элемент текста всплывающего окна
    print(alert.text.split()[-1])  # вывести последний элемент текста всплывающего окна
    alert.accept()
finally:
    time.sleep(30)
    browser.quit()