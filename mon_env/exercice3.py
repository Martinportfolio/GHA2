from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-position=2000,0")

#element le plus important
#permet d'interagir avec les site webs
driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demoqa.com/sortable")

driver.implicitly_wait(10)
driver.maximize_window()

actions = ActionChains(driver)
item_parent = driver.find_element(By.ID, 'demo-tabpane-list')
items = item_parent.find_elements(By.CLASS_NAME, 'list-group-item.list-group-item-action')

index = random.randint(0, len(items) -1)
index2 = random.randint(0, len(items) -1)

actions.drag_and_drop(items[index], items[index2]).perform()

time.sleep(5)

item_parent = driver.find_element(By.ID, "demo-tabpane-list")
nouvel_ordre = [item.text for item in item_parent.find_elements(By.CLASS_NAME, 'list-group-item.list-group-item-action')]
print("nouvel ordre :", nouvel_ordre)

driver.quit()