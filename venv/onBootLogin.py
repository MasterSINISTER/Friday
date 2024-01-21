import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import requests

driver=webdriver.Edge()
driver.get("http://172.16.1.1:8090/")
WuserName=driver.find_element(By.ID,"username")
WuserName.send_keys("MCA1003923")
WPassword=driver.find_element(By.ID,"password")
WPassword.send_keys("8359834412")
WPassword.send_keys(Keys.ENTER)
time.sleep(3)
driver.quit()
