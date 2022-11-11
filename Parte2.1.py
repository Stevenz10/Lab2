from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome('C:/Selenium/chromedriver')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")

time.sleep(2)
#select item with id twotabsearchtextbox
search_item = driver.find_element(By.ID,"twotabsearchtextbox")
search_item.send_keys("HP Pavilion azul")
#click search button
search_button = driver.find_element(By.ID,"nav-search-submit-button")
search_button.click()
time.sleep(3)

#select first item in amazon search
first_item = driver.find_element(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
first_item.click()
