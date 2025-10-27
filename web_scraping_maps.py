from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.FirefoxOptions()
options.add_argument('--headless')



driver = webdriver.Firefox(options=options)
driver.get("https://www.google.com/maps/")
driver.maximize_window()
search_result = driver.find_element(By.ID,"searchboxinput")
search_result.send_keys("store name goes here")
search_result.send_keys(Keys.ENTER)
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-label='store name goes here']"))).click()
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,"//*[@aria-label='Reviews for store name goes here']"))).click()
time.sleep(3)
more_button_list = []
review = []
review_list = driver.find_element(By.XPATH, "//div[contains(@class, 'm6QErb DxyBCb kA9KIf dS8AEf XiKgde ')]")
height_old = driver.execute_script("return arguments[0].scrollHeight;", review_list)

while True:
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", review_list)
    time.sleep(4)
    height_new = driver.execute_script("return arguments[0].scrollHeight;", review_list)
    if height_new== height_old:
        break
    height_old=height_new

more_buttons = driver.find_elements(By.XPATH, "//*[@aria-label='See more']")
for i in range(0,len(more_buttons)):
    more_buttons[i].click()
review_texts = driver.find_elements(By.CSS_SELECTOR, "span.wiI7pd")
for i in range(0,len(review_texts)):
    review.append(review_texts[i].text)
df = pd.DataFrame(review)
df.to_csv('reivews.csv', index=False)
time.sleep(2)
driver.quit()

