from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import selenium

browser = webdriver.Chrome(r"D://soft/python/chromedriver_win32/chromedriver")
browser.get("https://web.whatsapp.com")
wait = WebDriverWait(browser,600)
#target='"name"'
target='"NAME"'# replace NAME with name of your contact in your phone whatsapp
message= "Hi phone chalatoy ka tuza"
x_arg='//span[contains(@title, '+target+')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box = browser.find_element_by_class_name("_1Plpp")
for i in range(100):
    input_box.send_keys(message + Keys.ENTER)




#aboutus=driver.find_element_by_link_text("About Us")
#aboutus.click()