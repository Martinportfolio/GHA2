from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-position=2000,0")

#element le plus important
#permet d'interagir avec les site webs
driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://demoqa.com/text-box")
inputname ="john Doe"

fullname = driver.find_element(By.ID, "userName")
fullname.send_keys(inputname)
fullEmail = driver.find_element(By.ID, "userEmail")
fullEmail.send_keys("john.Doe@gmail.com")
fullcurrentAddress = driver.find_element(By.ID, "currentAddress")
fullcurrentAddress.send_keys("38 rue jean jaures")
fullpermanentAddress = driver.find_element(By.ID, "permanentAddress")
fullpermanentAddress.send_keys("38 rue jean jaures")
submit = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()

time.sleep(2)

submitted_name = driver.find_element(By.ID, "name")

assert inputname in submitted_name.text

time.sleep(5)

driver.quit()