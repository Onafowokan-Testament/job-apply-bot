from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time
from selenium.common.exceptions import NoSuchElementException
email ="onafowokan.testament@stu.cu.edu.ng"
password = os.environ.get("password")
url = "https://www.linkedin.com/jobs/search/?currentJobId=3213591032&f_AL=true&f_E=1%2C2&f_T=25169%2C9%2C25201&f_WT=2&" \
      "geoId=103644278&keywords=python%20developer&location=United%20States&refresh=true"
chrome_driver_Path = r"C:\Users\USER\Documents\PYTHON\DOWNLOADS\chromedriver.exe"
s= Service(chrome_driver_Path)
driver = webdriver.Chrome(service =s)
driver.maximize_window()


driver.get(url)
time.sleep(5)
sign_in_button =driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

user_name = driver.find_element(By.ID, "username")
user_name.send_keys(email)

web_password = driver.find_element(By.ID, "password")
web_password.send_keys(password)

second_sign_in = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button')
second_sign_in.click()
all_jobs = driver.find_elements(By.CSS_SELECTOR,".jobs-search-results__list-item")
for job in all_jobs:

      try:
            job.click()
            time.sleep(4)
            apply_button = driver.find_element(By.CLASS_NAME, 'jobs-apply-button')
            apply_button.click()
            time.sleep(3)
            button = driver.find_element(By.CSS_SELECTOR, "form button span")
            button_text = button.text
            print(button_text)

            if button_text == "Next":
                  print('Not Easy Application')
                  cancel = driver.find_element(By.CLASS_NAME,"mercado-match")
                  cancel.click()
                  time.sleep(1)
                  approval = driver.find_element(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")
                  approval.click()


            else:
                  submit = driver.find_element(By.XPATH, '//*[@aria-label="Submit application"]')
                  submit.click()
                  continue


      except NoSuchElementException as e:
            print("Error")
            continue