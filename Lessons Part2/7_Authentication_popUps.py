import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=myServices)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")










input("Enter any key to exit.........")
driver.quit()