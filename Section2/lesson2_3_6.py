from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    bro = webdriver.Chrome()
    bro.get(link)

 # Нажимаем кнопку
    button1 = bro.find_element_by_css_selector("button.trollface").click()
    
 # Работаем со второй вкладкой
    new_window = bro.window_handles[1]
    bro.switch_to.window(new_window)
    
 # Расчитываем значение Х
    y = calc(bro.find_element_by_id("input_value").text)

 # Заполняем строку
    input1 = bro.find_element_by_id('answer').send_keys(y) 
    
 # Нажимаем кнопку   
    button2 = bro.find_element_by_css_selector("button.btn").click()
    
 # Выводим ответ
    answer = bro.switch_to.alert
    print(answer.text.split()[-1])
    answer.accept()
    
 
finally:
 # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
 # закрываем браузер после всех манипуляций
    bro.quit()
    



