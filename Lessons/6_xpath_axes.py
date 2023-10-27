
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

myServices = Service("C:\Drivers_i_downloaded\chromedriver-win64\chromedriver-win64\chromedriver.exe")
myXpath = webdriver.Chrome(service=myServices)
myXpath.get("https://money.rediff.com/gainers/bse/daily/groupa")
# todo This method is used to maximize or expand the window size
myXpath.maximize_window()
# todo Adding implicit wait to wait for up to some seconds when trying to find an element before throwing a TimeoutException)
myXpath.implicitly_wait(20)

# todo Self
textFromPage = myXpath.find_element(By.XPATH, "//a[contains(text(),'ITI')]/self::a").text
print(textFromPage)

# todo Parent
textFromPage = myXpath.find_element(By.XPATH, "//a[contains(text(),'ITI')]/parent::td").text
print(textFromPage)

# todo Child-----since we cannot get child directly from the self of the webpage, we consider the ancestor element,use it to get the child element
textFromPage = myXpath.find_elements(By.XPATH, "//a[contains(text(),'ITI')]/ancestor::tr/child::td")
for item in textFromPage:
    print(item.text)

# todo Ancestor
textFromPage = myXpath.find_element(By.XPATH, "//a[contains(text(),'ITI')]/ancestor::tr").text
print(textFromPage)

# todo Descendant
textFromPage = myXpath.find_elements(By.XPATH, "//a[contains(text(),'ITI')]/ancestor::tr/descendant::*")
for descendant in textFromPage:
    print(descendant.text)

# todo Following
textFromPage = myXpath.find_elements(By.XPATH, "//a[contains(text(),'ITI')]/ancestor::tr/following::*")
print(f"There are {len(textFromPage)}  of descending nodes")

# todo Following-Sibling
following_sibling = myXpath.find_elements(By.XPATH, "//a[contains(text(),'ITI')]/ancestor::tr/following-sibling::*")
print(f"There are {len(following_sibling)}  of following-sibling nodes")

# todo Preceding
precedings = myXpath.find_elements(By.XPATH, "//a[contains(text(),'ITI')]/ancestor::tr/preceding::*")
print(f"There are {len(precedings)}  of preceding nodes")

# todo Preceding-siblings
preceding_siblings = myXpath.find_elements(By.XPATH, "//a[contains(text(),'ITI')]/ancestor::tr/preceding::*")
print(f"There are {len(preceding_siblings)}  of preceding-siblings nodes")

input("press any key to terminate process...")
myXpath.quit()

