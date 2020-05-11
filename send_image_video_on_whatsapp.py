from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
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
file_path = input("Enter path of image")
message= input("Enter the message")
input_box = browser.find_element_by_class_name("_39LWd")
attachment_section = browser.find_element_by_xpath('//div[@title="Attach"]')
attachment_section.click()

image=browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
image.send_keys(file_path)
sleep(3)
send_button = browser.find_element_by_xpath('//span[@data-icon="send-light"]')
input_box.send_keys(message)
send_button.click()
