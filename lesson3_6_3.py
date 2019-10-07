import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('links', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class TestMath(object):
    def test_find_correct_link_for_answer(self, browser, links):
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)

        answer = math.log(int(time.time()))

        text_field = browser.find_element_by_xpath('//textarea [@placeholder="Напишите ваш ответ здесь..."]')
        input1 = text_field.send_keys(str(answer))
        button = browser.find_element_by_xpath('//button [@class="submit-submission "]').click()

        correct = browser.find_element_by_xpath('//pre [@class="smart-hints__hint"]').text
        assert correct == "Correct!", correct




