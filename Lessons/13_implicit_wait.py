from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()

# todo Adding implicit wait to wait for up to some seconds when trying to find an element before throwing a TimeoutException)
myDriver.implicitly_wait(20)
myDriver.get("https://google.com")
searchBox = myDriver.find_element(By.ID, "APjFqb")
searchBox.send_keys("Selenium")
searchBox.submit()
myDriver.find_element(By.XPATH, '//*[@id="rso"]/div[6]/div/div/div[1]/div/div/span/a/h3').click()






input("Enter a value to terminate process...")
myDriver.quit()




