# from selenium import webdriver

# driver = webdriver.Firefox()

# driver.implicitly_wait(10)
# driver.get("https:\\example.com")
# element = driver.find_element("id", "some_id")

#------------------------------------>
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

#set implicity wait 
driver.implicitly_wait(10)

driver.get("https://www.wikipedia.org/")

# Try finding the search input (if not immediately present, it will wait) 
search_box = driver.find_element(By.ID, "searchInput") .send_keys("Selenium WebDriver") 
search_button = driver.find_element(By.XPATH, "//button[@type='submit']") 
search_button.click() 
print("Page Title:", driver.title)
driver.quit()