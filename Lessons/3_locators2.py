
from selenium import  webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\edgedriver_win64/msedgedriver.exe")
myDriver = webdriver.Edge(service=myServices)
myDriver.get("https://ultimateqa.com/dummy-automation-websites/")
# todo This method is used to maximize or expand the window size
myDriver.maximize_window()
# todo Adding implicit wait(wait for up to some seconds when trying to find an element before throwing a TimeoutException)
myDriver.implicitly_wait(20)
# todo To find the total number of images sliders in a web homepage
# numberOfSlider = myDriver.find_elements(By.CLASS_NAME, "  ")
# print(len(numberOfSlider))
# todo To find the total number of links in a webpage
numberOfLinksInWebpage = myDriver.find_elements(By.TAG_NAME, "a")
lenfthOfThePage = len(numberOfLinksInWebpage)
print(f"There are {lenfthOfThePage} links in this webpage")

input("Press Enter to close the browser...")
myDriver.quit()

