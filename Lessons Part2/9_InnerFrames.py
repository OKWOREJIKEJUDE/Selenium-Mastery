from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=myServices)
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']").click()
# todo ---Outer frame
outerFrame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)
# todo ---Inner frame
innerFrame = driver.find_element(By.CSS_SELECTOR, "iframe[src='SingleFrame.html']")
driver.switch_to.frame(innerFrame)
# todo ---text fielf inside the inner frame
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Callistus Jude")
# todo ---The below command will switch back to the frame you came from(Parent Frame)
driver.switch_to.parent_frame()
# todo ---Then if there other items in the parent freme, you handle it.........










input("Enter any key to exit.........")
driver.quit()