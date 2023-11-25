from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=myServices)
driver.maximize_window()
driver.implicitly_wait(20)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# todo Current window handle
singleWindowId = driver.current_window_handle
print("Single windowID is: ", singleWindowId)

# # todo multiple browser windows ---- APPROACH 1
driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
multipleWindowsID = driver.window_handles
# # print("Multiple windowsID's are: ", multipleWindowsID[:]) # --- [:]->This means print everything in the list
# firstWindow = multipleWindowsID[0]  # -- First browser windowID
# secondWindow = multipleWindowsID[1]  # -- Second browser windowID
# # todo Switching from first browser window to second browser window
# driver.switch_to.window(secondWindow)
# print("Title of the second window is : ", driver.title)
# # todo Switching from second browser window back to first browser window
# driver.switch_to.window(firstWindow)
# print("Title of the first window is : ", driver.title)


# # todo multiple browser windows ---- APPROACH 2
# for wind in multipleWindowsID:
#     driver.switch_to.window(wind)
#     print("Switched successfully, New browser window:", driver.title)

# todo Closing specific browser windows when you have a lot of them open
for window in multipleWindowsID:
    driver.switch_to.window(window)  # -- switching to a particular window
    if driver.title == "OrangeHRM HR Software | OrangeHRM":  # --- if the title of the page is "OrangeHRM HR Software | OrangeHRM", then close browser
        driver.close()










input("Enter any key to exit.........")
driver.quit()
