from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()

myDriver.implicitly_wait(20)
myDriver.get("https://testautomationpractice.blogspot.com/")

# # todo 1. Select Specific checkbox
# myDriver.find_element(By.XPATH, "//input[@type='checkbox']").click()

# todo 2. Select all the checkboxes
multipleCheckbox = myDriver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(multipleCheckbox))
#Appproach1
# for checkbox in multipleCheckbox:
#     checkbox.click()

# #Appproach2
# for check in range(len(multipleCheckbox)):
#     multipleCheckbox[check].click()

# # todo 3. Select multiple checkboxes by choice
# for checkbox in multipleCheckbox:
#     weekname = checkbox.get_attribute("id")
#     if weekname == "monday" or weekname == "wednesday" or weekname == "saturday":
#         checkbox.click()


# # todo 3. Select last two checkboxes
# # The formula for this is ===[Total number of indexes - 2(because of last two you're selecting)]
# # If it is last three==== Total number of indexes - 3(because of last three you're selecting)
# # todo In the below example, 7-2 = 5, therefore we are starting from index 5
# lengthOfCheckboxes = len(multipleCheckbox) # to get the total length of checkboxes
# for i in range(lengthOfCheckboxes - 2, lengthOfCheckboxes): # this means range(5, 7)
#     multipleCheckbox[i].click()


# todo 3. Select first two checkboxes
# The formula for this is == range(0,2)..because you are accessing from 0 to 2. Now below is how to do it in code
# todo In the below example, 7-7 = 0, and 7-5 = 2. range(0,2) therefore we are starting from index 0 until 2
lengthOfCheckboxes = len(multipleCheckbox) # to get the total length of checkboxes = 7
for i in range(lengthOfCheckboxes - 7, lengthOfCheckboxes - 4): # this means range(5, 7)
    multipleCheckbox[i].click()







input("Enter a value to terminate process...")
myDriver.quit()




