from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()
myDriver.get("https://admin-demo.nopcommerce.com/login")

textt = myDriver.find_element(By.ID, "Email")
textt.clear()
textt.send_keys("ejike.okwor.247590@unn.edu.ng")
print("Result of text:", textt.text)
print("Result of get_attribute:", textt.get_attribute('value'))

# todo NB text keyword is used to return the inner text of the html but geta_attribute is used to return thw actual text written on the space provided










input("Enter a value to terminate process...")
myDriver.quit()