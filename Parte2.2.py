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
time.sleep(2)

#select first item in amazon search
first_item = driver.find_element(By.XPATH,"//span[@class='a-size-medium a-color-base a-text-normal']")
first_item.click()
time.sleep(5)

dropdown = driver.find_element(By.XPATH,'//*[@id="a-autoid-0-announce"]/span[1]')
print(dropdown.text)
dropdown.click()

#select quantity dropdown in amazon product
quantity_dropdown = driver.find_element(By.XPATH,'//*[@id="quantity_1"]')
print(quantity_dropdown.text)
quantity_dropdown.click()
time.sleep(2)


add_cart = driver.find_element(By.ID,"add-to-cart-button")
add_cart.click()

cart = driver.find_element(By.XPATH,'//*[@id="nav-cart-count"]')
cart.click()