from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()

myDriver.implicitly_wait(50)
myDriver.get("https://demo.nopcommerce.com/")

# todo 1. Click on link
# myDriver.find_element(By.LINK_TEXT, "Digital downloads").click()

# todo 2. Find total number of links in a pag
# todo 3. Links are identified with/by tag name. [The below code means we're printing the total number of links in the page]
# links = myDriver.find_elements(By.TAG_NAME, "a")
links = myDriver.find_elements(By.XPATH, "//a")
print(f"Total number of links in this page are: {len(links)}")

# todo 4. Print/display all the link names
for displayLinks in links:
    print(displayLinks.text)

# todo 5.













input("Enter any key to exit.........")
myDriver.quit()