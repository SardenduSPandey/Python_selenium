from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as WaitE


browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.180.36/Common/Login.aspx")
'login into application'
browser.find_element_by_id("body_txtUserID").send_keys("donhere")
browser.find_element_by_name("ctl00$body$txtPassword").send_keys("don@123")
'explicit wait'
WebDriverWait(browser,2).until(WaitE.element_to_be_clickable((By.ID,"body_btnLogin")))

browser.find_element_by_id("body_btnLogin").click()

'implicit wait'
browser.implicitly_wait(3)

print(browser.find_element_by_id("divWelcome").text)