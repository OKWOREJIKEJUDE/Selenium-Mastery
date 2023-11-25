from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver.exe")
conditional_commands = webdriver.Chrome(service=myServices)
conditional_commands.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# todo This method is used to maximize or expand the window size
conditional_commands.maximize_window()
# todo Adding implicit wait to wait for up to some seconds when trying to find an element before throwing a TimeoutException)
conditional_commands.implicitly_wait(20)


# todo is_displayed()....[to check wether the searchbox is displayed on the webpage]
searchbox = conditional_commands.find_element(By.XPATH, '//*[@id="small-searchterms"]')
print(searchbox.is_displayed(), ".....searchbox is properly displayed")

# todo is_enabled()....[to check wether the searchbox is enabled/is allowing us to click on it.]
searchbox = conditional_commands.find_element(By.XPATH, '//*[@id="small-searchterms"]')
print(searchbox.is_enabled(), ".....searchbox allows us to click on it")

# todo is_selected()....[to check wether the Radio buttons and checkboxes is/are selected.]
male_radioButton = conditional_commands.find_element(By.XPATH, '//*[@id="gender-male"]')
female_radioButton = conditional_commands.find_element(By.XPATH, '//*[@id="gender-female"]')
print(male_radioButton.is_selected(), "..... Male is not clicked")
print(female_radioButton.is_selected(), "..... Female is not clicked")
# when i select male radio button
male_radioButton.click()
# the result
print(male_radioButton.is_selected(), ".....Male is now clicked/selected")
print(female_radioButton.is_selected(), ".....Female is now clicked/selected")





input("Press any key to terminate process...")
conditional_commands.quit()