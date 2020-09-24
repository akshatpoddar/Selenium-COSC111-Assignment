from selenium import webdriver
import os
import sys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

FILE_PATH = sys.argv[2]
PATH = os.getcwd()+"/chromedriver"
driver = webdriver.Chrome(PATH)
ASS_NUMBER = sys.argv[1]
SLUG = 642720 + (2*int(ASS_NUMBER))
URL = "https://canvas.ubc.ca/courses/63432/assignments/"+str(SLUG)
NAME = "Assignment " + ASS_NUMBER


USERNAME = sys.argv[3]
PASSWORD = sys.argv[4]


#navigating to webpage
driver.get(URL)
print(f"Visiting {URL}")
driver.implicitly_wait(20)

#logging into account
print("Logging in as " + USERNAME)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[1]/form/div[1]/input").send_keys(USERNAME)
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div/div[1]/form/div[2]/input").send_keys(PASSWORD)
driver.find_element_by_xpath("//button[@type='submit']").click()
driver.implicitly_wait(20)

#uploading the file
print(f"Uploading {NAME}...")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[1]/div[1]/div[2]/button").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/form/table/tbody/tr[2]/td[2]/div[1]/input").send_keys(FILE_PATH)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div/form/table/tbody/tr[5]/td/button[2]").click()
time.sleep(10)

print("FILE UPLOADED SUCCESSFULLY!")

#logging out
driver.find_element_by_xpath("/html/body/div[2]/header[2]/div[1]/ul/li[1]/a").click()
driver.implicitly_wait(2)
driver.find_element_by_xpath("/html/body/div[3]/span/span/div/div/div/div/div/span/form/button").click()
time.sleep(5)

driver.quit()
print("Quitting...")
