from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=myServices)
driver.maximize_window()
driver.implicitly_wait(20)
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.frame("frame-one796456169")
driver.find_element(By.NAME, "RESULT_TextField-0").send_keys("Okwor Ejike Jude")
driver.switch_to.default_content() # ---to switch back to the page before entering another iframe
# todo Then if there is any other iframes in the website, then we enter again with the switch command










input("Enter any key to exit.........")
driver.quit()