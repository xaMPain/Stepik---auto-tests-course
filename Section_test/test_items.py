import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_different_language(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_xpath('//button [@class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert button.get_attribute("type") == "submit", "Ошибка"