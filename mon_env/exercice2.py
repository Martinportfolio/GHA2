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

driver.get("https://www.selenium.dev")

driver.maximize_window()

time.sleep(10)

print("La page " + driver.current_url + " a été trouvé")
print("le titre est " + driver.title)

try:
    driver.find_element(BY.ID, "n'éxiste pas")
except:
    print("L'élément n'existe pas")
    assert False, "Lélément n'éxiste pas"

element = driver.find_element(By.CSS_SELECTOR, "a[Href='/documenttation']")

if (element):
    element[0].click()
else:
    assert False
    