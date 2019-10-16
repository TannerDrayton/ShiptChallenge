import time
from selenium import webdriver

driver = webdriver.Chrome('/Users/tannerriddle/Desktop/chromedriver')
driver.get('https://shop.shipt.com/login')
time.sleep(3)
username_box = driver.find_element_by_name('username')
username_box.send_keys('js0674405@gmail.com')
password_box = driver.find_element_by_name('password')
password_box.send_keys('JohnSmith01')
login_box = driver.find_element_by_class_name('LoXaa')
login_box.submit()
time.sleep(3)
driver.quit()