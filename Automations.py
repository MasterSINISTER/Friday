from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def leetCodeLogin():
    driver = webdriver.Edge()
    driver.get("https://leetcode.com/accounts/login/")

    driver.implicitly_wait(10)

    username = driver.find_element(By.ID, "id_login")
    username.send_keys("MasterSi")

    password = driver.find_element(By.ID, "id_password")
    password.send_keys("imt#Ebestdude@30me")

    submit = driver.find_element(By.ID, "signin_btn")
    submit.click()

    WebDriverWait(driver, 10).until(EC.url_to_be("https://leetcode.com/"))

    while True:
        time.sleep(1)
leetCodeLogin()