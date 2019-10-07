from selenium import webdriver
import unittest


class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # заполняем данные
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']").send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']").send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']").send_keys("Smolensk")
        input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']").send_keys("666")
        input5 = browser.find_element_by_css_selector("[placeholder='Input your address:']").send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn").click()

        # проверяем результат
        recived_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", recived_text)

        browser.close()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # заполняем данные
        input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']").send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']").send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("[placeholder='Input your email']").send_keys("Smolensk")
        input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']").send_keys("666")
        input5 = browser.find_element_by_css_selector("[placeholder='Input your address:']").send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn").click()

        # проверяем результат
        recived_text = browser.find_element_by_tag_name("h1").text
        self.assertEqual("Congratulations! You have successfully registered!", recived_text)


        browser.close()
        browser.quit()

if __name__ == "__main__":
    unittest.main()