import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=myServices)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://mypage.rediff.com/login/dologin")

driver.find_element(By.XPATH, "//input[@value='Login']").click()
time.sleep(2)
myAlert = driver.switch_to.alert
print("The text present in the alert window is: ", myAlert.text)
myAlert.accept()











input("Enter any key to exit.........")
driver.quit()