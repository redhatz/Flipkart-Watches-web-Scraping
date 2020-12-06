from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = (r"C:\Users\redhatz\Desktop\assignment\chromedriver.exe")
finalwatches=[]

driver=webdriver.Chrome(PATH)
driver.get("https://www.flipkart.com/")

search = driver.find_element_by_name("q")
search.send_keys("watches")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div/section[4]/div[2]/div[1]/div[3]/div/div/label/div[1]')))
    el=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[1]/div/section[4]/div[2]/div[1]/div[3]/div/div/label/div[1]')
    driver.execute_script("arguments[0].click();", el)
    
    time.sleep(1)
    likes = driver.find_elements_by_class_name("IRpwTa")
    time.sleep(1)
    print("List of watches from the page are \n")
    for like in likes:
        print(like.get_attribute("title"))
        finalwatches.append(like.get_attribute("title"))
    
    n = int(input("Enter a number to search the list of watches "))
    print("The name of watch at that position is "+finalwatches[n-1])

    
    
finally:
    driver.close()