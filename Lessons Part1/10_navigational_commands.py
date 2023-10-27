from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
navigational_commands = webdriver.Chrome(service=myServices)
navigational_commands.maximize_window()
navigational_commands.get("https://snapdeal.com/")
navigational_commands.get("https://www.amazon.com/")

# todo back, forward and refresh is used to navigate to and fro on the webpage
navigational_commands.back()
navigational_commands.forward()
navigational_commands.refresh()







input("click any key to terminate...")
navigational_commands.quit()

