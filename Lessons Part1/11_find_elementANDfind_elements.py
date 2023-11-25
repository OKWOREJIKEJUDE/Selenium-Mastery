from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()
myDriver.get("https://demo.nopcommerce.com")

# # todo SCENARIOS OF FIND ELEMENT TO CHECK
# # todo 1. Locator matching with single web element
# element = myDriver.find_element(By.XPATH, '//*[@id="small-searchterms"]')
# element.send_keys("Apple MacBook Pro 13-inch")
#
# # todo 2. Locator matching with multiple web element
# # todo in this example, we used a keyword say "footer" to capture all the links we want.Type "//div[@class='footer']//a" on the selector hub space to highlight them
# element = myDriver.find_element(By.XPATH, "//div[@class='footer']//a") # this will return multiple web elements. among the elements returned, the first one only will display b/c of our keyword element
# print(element.text)
#
# # todo 3. Element not available, then throw NoSuchElementException
# # todo findElement throws an exception once the key is wrong(LINK_TEXT is not complete)
# element = myDriver.find_element(By.LINK_TEXT, "Log")
# element.click()

# # todo SCENARIOS OF FIND ELEMENT TO CHECK
# # todo 1. Locator matching with single web element
# # todo Here, we used a single locator "//*[@id="small-searchterms"]" to access multiple web elements (by find_elements)
# elementss = myDriver.find_elements(By.XPATH, '//*[@id="small-searchterms"]')# todo send_keys method won't appear b/c we're pointing at multiple elements
# print(len(elementss))
# print(elementss[0].send_keys("Apple MacBook Pro 13-inch"))

# # todo 2. Locator matching with multiple web element
# # todo we used a single locator to access multiple web elements(find_elements) and the printer the one we wanted
# ourElement = myDriver.find_elements(By.XPATH, "//div[@class='footer']//a")
# print(len(ourElement))
# print(ourElement[0].text)
#
# for elem in ourElement:
#     print(elem.text)

# todo 3. Element will not throw NoSuchElementException
# todo Here, even if the locator (Lo) is wrong, it will not throw any exception, it will return element 0
exceptionElement = myDriver.find_elements(By.LINK_TEXT, "Lo")
print("Elements returned =", len(exceptionElement))




input("click any key to terminate...")
myDriver.quit()

