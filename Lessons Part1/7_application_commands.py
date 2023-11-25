from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
application_command = webdriver.Chrome(service=myServices)
application_command.get("https://www.orangehrm.com/")
# todo This method is used to maximize or expand the window size
application_command.maximize_window()
# todo Adding implicit wait to wait for up to some seconds when trying to find an element before throwing a TimeoutException)
application_command.implicitly_wait(20)

print(application_command.title)
print(application_command.current_url)
print(application_command.page_source)



input("Press any key to terminate process...")
application_command.quit()


