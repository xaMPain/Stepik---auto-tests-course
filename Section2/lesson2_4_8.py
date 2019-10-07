from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

bro = webdriver.Chrome()
bro.get("http://suninjuly.github.io/explicit_wait2.html")

# ������� Selenium ��������� � ������� 5 ������, ���� ���� �� ������ 100
price = WebDriverWait(bro, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
bro.find_element_by_id("book").click()
    
# ������ ������
y = calc(bro.find_element_by_id("input_value").text)

 # ��������� ������
input1 = bro.find_element_by_id('answer').send_keys(y) 
    
 # �������� ������   
button2 = bro.find_element_by_id("solve").click()  

# ������� �����
answer = bro.switch_to.alert
print(answer.text.split()[-1])
answer.accept()

# ��������� ������� ����� ���� �����������
bro.quit()
