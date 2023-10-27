#TEST CASE
#1. Open web browser(chrome/firefox/edge)
#2. Open URL https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
#3. Provide username (Admin)
#4. Provide password (admin123)
#5. Click on Login
#6. Capture title of the dashboard page (Actual title)
#7. Verify title of the page: "OrangeHRM" (Expected)
#8. Close browser


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# myService = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# myDriver = webdriver.Chrome(service=myService)

# Use the single below code when you must have put drivers inside the location you installed python
myDriver = webdriver.Firefox()
# Adding implicit wait(wait for up to some seconds when trying to find an element before throwing a TimeoutException)
myDriver.implicitly_wait(20)
myDriver.get("https://opensource-demo.orangehrmlive.com/")
myDriver.find_element(By.NAME, "username").send_keys("Admin")
myDriver.find_element(By.NAME, "password").send_keys("admin123")
myDriver.find_element(By.CSS_SELECTOR, ".oxd-button.oxd-button--medium.oxd-button--main.orangehrm-login-button").click()
# Check the title of the webpage
titleOfThePage = myDriver.title
expectedTitle = "OrangeHRM"
if titleOfThePage == expectedTitle:
    print("Login test passed")
else:
    print("Login Test failed")
input("Press Enter to close the browser...")
myDriver.quit()












