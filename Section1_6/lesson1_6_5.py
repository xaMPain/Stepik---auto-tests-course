from selenium import webdriver


try:
    link = "http://suninjuly.github.io/find_link_text"
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # переключиться на всплывающее окно
    alert = browser.switch_to.alert
    # вывести последний элемент текста всплывающего окна
    print(alert.text.split()[-1])  # вывести последний элемент текста всплывающего окна
    alert.accept()

finally:
    browser.close()
    browser.quit()