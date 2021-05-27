from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://google.com")

xpath = "//div[@class='FPdoLc lJ9FBc']//input[@name='btnI']"
falseXpath = "//dv[@class='FPdoLc lJ9FBc']//input[@name='btnI']"

if driver.find_elements_by_xpath(falseXpath): # then try with correct xpath
    print("xpath found")
    driver.find_element_by_xpath(falseXpath).click() #then try with Correct xpath

else:
    print("xpath not found")
