from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://rapsodo.com/")

driver.maximize_window()

driver.implicitly_wait(20)
shopNow = driver.find_element(By.LINK_TEXT, "SHOP NOW")
shopNow.click()

driver.implicitly_wait(20)
diamondSports = driver.find_element(By.LINK_TEXT, "Diamond Sports")
diamondSports.click()

print("\n")
print("Diamond Sports Link ==>", driver.current_url)

items = driver.find_element(By.CLASS_NAME, "Description")

print("\n")
print("Items-Price Amount==>", items.text)

driver.implicitly_wait(20)
element = driver.find_element(By.XPATH, "//*[@id='main']/div/ul/li[2]/div[1]/a")
element.click()

print("\n")
print("Hitting Monitor Url Link ==>", driver.current_url)

print("\n")
print(driver.title)

driver.implicitly_wait(20)
element = driver.find_element(By.XPATH, "//*[@id='product-386']/div[2]/div[2]/div/form/button")

prop = element.get_property('disabled')

print("\n")
print("Add To Cart Button is disabled ? ==>", prop)



# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "cookie-law-info-bar"))).click()
#
# #WebDriverWait(driver, 20).until(EC.invisibility_of_element((By.CSS_SELECTOR, "button[type='submit']"))).click()
#
#
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='CloudModal']/div/div/div[2]/div[2]/div[1]/div[4]/form/button"))).click()
#
#
#
# print("\n")
# print("Make It Bundle Link ==>", driver.current_url)
#
# items = driver.find_element(By.CLASS_NAME, "Description")
#
# print("\n")
# print("Items-Price Amount==>", items.text)
#
# element = driver.find_element(By.XPATH,"//*[@id='primary']/div[2]/div[1]/div/div/a")
# element.click()
#
# items = driver.find_element(By.NAME, "coupon_code")
# items.send_keys("11111111")
#
#
# items = driver.find_element(By.NAME, "apply_coupon")
# items.click()


driver.close()
