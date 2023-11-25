import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=myServices)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[onclick='jsPrompt()']").click()
alertWindow = driver.switch_to.alert
print("The text present in the alert window is: ", alertWindow.text)
alertWindow.send_keys("Okwor Ejike Jude")
time.sleep(2)
alertWindow.accept()  # for button OK when the Alert Appears
# alertWindow.dismiss()  # for button CANCEL when the Alert Appears














input("Enter any key to exit.........")
driver.quit()