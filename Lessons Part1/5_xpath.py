
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
myDriverForXpathPractice = webdriver.Chrome(service=myServices)
myDriverForXpathPractice.get("https://www.jumia.com.ng/")
# todo This method is used to maximize or expand the window size
myDriverForXpathPractice.maximize_window()
# todo Adding implicit wait to wait for up to some seconds when trying to find an element before throwing a TimeoutException)
myDriverForXpathPractice.implicitly_wait(20)

myDriverForXpathPractice.find_element(By.XPATH, '//*[@id="fi-q"]').send_keys("Television")
myDriverForXpathPractice.find_element(By.XPATH, '//*[@id="search"]/button').click()

input("press enter key to terminate process...")
myDriverForXpathPractice.quit()