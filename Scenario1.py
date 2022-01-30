from selenium import webdriver
import time

'open the chrome driver'
browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")

'open the application'
browser.get("http://10.82.180.36/Common/Login.aspx")

'maximize browser'
browser.maximize_window()

'refresh browser'
browser.refresh()

'fetch the title'
print("The title of the browser is "+browser.title)

'Current Url'

print("The current url before login "+browser.current_url)

'login functions'
browser.find_element_by_id("body_txtUserID").send_keys("donhere")

browser.find_element_by_name("ctl00$body$txtPassword").send_keys("don@123")

time.sleep(3)

browser.find_element_by_id("body_btnLogin").click()

'Current url'
print("the current url after login "+browser.current_url)

'back option'
browser.back()

'close the browser'
browser.close()