import time
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
browser_commands = webdriver.Chrome(service=myServices)
browser_commands.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# todo This method is used to maximize or expand the window size
browser_commands.maximize_window()
# todo Adding implicit wait to wait for up to some seconds when trying to find an element before throwing a TimeoutException)
browser_commands.implicitly_wait(20)

# todo close.... command is used to close a single browser window where the browser is focused.
browser_commands.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
time.sleep(5)
browser_commands.close()
time.sleep(5)

# todo quit..... command is used to terminate all the that opens the browser causing the browsers to close.
browser_commands.find_element(By.LINK_TEXT, 'OrangeHRM, Inc').click()
browser_commands.quit()