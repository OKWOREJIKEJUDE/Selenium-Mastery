from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()

myDriver.implicitly_wait(50)
myDriver.get("http://www.deadlinkcity.com/")



















input("Enter any key to exit.........")
myDriver.quit()