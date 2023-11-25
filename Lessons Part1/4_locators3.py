
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
d = webdriver.Chrome(service=myServices)
d.get("https://web.facebook.com/?_rdc=1&_rdr")
# todo This method is used to maximize or expand the window size
d.maximize_window()
# todo Adding implicit wait(wait for up to some seconds when trying to find an element before throwing a TimeoutException)
d.implicitly_wait(20)
#d.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[2]/div/input").send_keys("Okwor Ejike Jude")
d.find_element(By.XPATH,'//input[@name="email"]').send_keys("Ejykeman")


input("Press Enter to close the browser...")
d.quit()

