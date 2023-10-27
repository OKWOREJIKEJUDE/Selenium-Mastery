from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()

# todo Adding implicit wait to wait for up to some seconds when trying to find an element before throwing a TimeoutException)
myDriver.implicitly_wait(20)
myDriver.get("https://google.com")







input("Enter a value to terminate process...")
myDriver.quit()




