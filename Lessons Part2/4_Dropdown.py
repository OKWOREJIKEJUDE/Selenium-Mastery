from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
myDriver = webdriver.Chrome(service=myServices)
myDriver.maximize_window()

myDriver.implicitly_wait(50)

# # todo PART A
# myDriver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# # To select object from dropdown list
# myDropdownSelect = Select(myDriver.find_element(By.XPATH, "//select[@name='DateOfBirthYear']"))
#
# # Select options from the dropdown (Approach 1)
# myDropdownSelect.select_by_visible_text("1997")
#
# # Select options from the dropdown (Approach 2)
# #myDropdownSelect.select_by_value("1997")
#
# #  Select options from the dropdown (Approach 3)
# # myDropdownSelect.deselect_by_index()  # ---This does not show in the html page. You have to count the index. 85 is when you count from 0, 1913,1914 --- 1997. It falls on 85
#
# # Capture all the options and print them
# allOptions = myDropdownSelect.options # (options was used to select all the things inside that dropdown and then we printed below)
# print(f"Total number of Options are: {len(allOptions)}")
# for opt in allOptions:
#     print(opt.text)
#
# # Select option from dropdown without using built In function or method
# for opt in allOptions:
#     if opt=="1997":
#         opt.click()
#         break


# todo PART B
myDriver.get("https://demo.opencart.com/index.php?route=account/register")
# NB Comment the upper part of the code before running the lower  part
# The code below will Open the dropdown and pick anything you want inside the dropdown
# We don't need to use select here because the tagName in the Html page is not select
myDriver.find_element(By.XPATH, "//a[normalize-space()='MP3 Players']").click()
myDriver.find_element(By.XPATH, "//a[normalize-space()='test 17 (0)']").click()










input("Enter any key to exit.........")
myDriver.quit()