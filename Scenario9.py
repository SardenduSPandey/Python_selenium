from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from logging import exception


browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.180.36/Common/Login.aspx")
'login into application'
browser.find_element_by_id("body_txtUserID").send_keys("donhere")
browser.find_element_by_name("ctl00$body$txtPassword").send_keys("don@123")
browser.find_element_by_id("body_btnLogin").click()
time.sleep(2)
browser.find_element_by_link_text("Contact Us").click()

' Window handle'
window_handle=browser.window_handles
print(len(window_handle))

for i in window_handle:
    browser.switch_to.window(i)
    print(browser.current_url)
result=browser.find_element_by_id("GeneralTabMenu_header_divHeader").text
print(result)





