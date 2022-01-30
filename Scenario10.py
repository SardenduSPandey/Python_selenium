from selenium import webdriver
import time
from logging import exception

'Exception Handling'
from selenium.common.exceptions import NoSuchElementException

browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.180.36/Common/Login.aspx")
'login into application'
browser.find_element_by_id("body_txtUserID").send_keys("donhere")
browser.find_element_by_name("ctl00$body$txtPassword").send_keys("don@123")
try:
    browser.find_element_by_id("body_btnLogi").click()
except NoSuchElementException as exception:
    print("locator value is incorrect, make sure that you have entered correct one")
time.sleep(2)