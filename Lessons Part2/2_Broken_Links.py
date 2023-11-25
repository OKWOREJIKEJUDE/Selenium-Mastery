from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  requests as requests

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()

myDriver.implicitly_wait(50)
myDriver.get("http://www.deadlinkcity.com/")

# todo We therefore installed request package through File--> Settings--> ProjectInterpreter..
links = myDriver.find_elements(By.XPATH, "//a")
print(f"The total number of links in this page is: {len(links)}")

count = 0
# todo To print out the links
for li in links:
    url = li.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print(f"This url: {url},  is a broken link")
        count = count+1
    else:
        print(f"This url: {url},  is not a broken link")

print("Total number of broken links is:", count)














input("Enter any key to exit.........")
myDriver.quit()