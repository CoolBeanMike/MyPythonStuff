#!/usr/bin/python

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(By.NAME, value="my-text")
submit_button = driver.find_element(By.CSS_SELECTOR, value="button")
drop_down_select = driver.find_element(By.CSS_SELECTOR, value="select")
file_input = driver.find_element(By.CSS_SELECTOR, value="input[type='file']")
choose_date = driver.find_element(By.NAME, value="my-date")
slider = driver.find_element(By.NAME, value="my-range")
my_password = driver.find_element(By.NAME, value="my-password")
my_textarea = driver.find_element(By.NAME, value="my-textarea")

text_box.send_keys("Selenium")
sleep(2)

drop_down_select.click()
sleep(2)

file_path = "C:\\temp\\test_file.txt"
file_input.send_keys(file_path)
sleep(2)

choose_date.send_keys("04/06/2025")
my_password.click()
my_textarea.click()

sleep(2)

actions = ActionChains(driver)
slider_width = slider.size['width']

min_value = int(slider.get_attribute('min'))
max_value = int(slider.get_attribute('max'))
current_value = int(slider.get_attribute('value'))
step = int(slider.get_attribute('step'))

target_value = 0
while target_value <= max_value:
    step_width = slider_width / ((max_value - min_value) / step)
    steps_to_move = target_value - current_value
    x_offset = steps_to_move * step_width
    actions.click_and_hold(slider).move_by_offset(x_offset,0).release().perform()
    sleep(1)
    target_value += 1

submit_button.click()
sleep(2)

message = driver.find_element(by=By.ID, value="message")
text = message.text

driver.quit()