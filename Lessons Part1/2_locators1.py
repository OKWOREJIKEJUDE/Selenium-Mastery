
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myOwnDriver = webdriver.Chrome(service=myServices)
myOwnDriver.get("https://demo.nopcommerce.com/")
# todo This method is used to maximize or expand the window size
myOwnDriver.maximize_window()
# todo Adding implicit wait(wait for up to some seconds when trying to find an element before throwing a TimeoutException)
myOwnDriver.implicitly_wait(20)
myOwnDriver.find_element(By.ID, "small-searchterms").send_keys("Apple MacBook Pro 13-inch")
myOwnDriver.find_element(By.CSS_SELECTOR, ".button-1.search-box-button").click()
myOwnDriver.find_element(By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button").click()
# myOwnDriver.find_element(By.LINK_TEXT, "Asus N551JK-XO076H Laptop").click()
myOwnDriver.find_element(By.NAME, "addtocart_4.EnteredQuantity").clear()
myOwnDriver.find_element(By.NAME, "addtocart_4.EnteredQuantity").send_keys("3")
myOwnDriver.find_element(By.ID, "add-to-cart-button-4").click()
myOwnDriver.find_element(By.CSS_SELECTOR, ".cart-label").click()

# todo How to use CLASS NAME
# lengthOfSliders = myOwnDriver.find_elements(By.CLASS_NAME, "        ")
# print(len(lengthOfSliders))


input("Press Enter to close the browser...")
myOwnDriver.quit()

