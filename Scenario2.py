from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
'Open the browser'

browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.180.36/Common/Login.aspx")
'login into application'
browser.find_element_by_id("body_txtUserID").send_keys("donhere")
browser.find_element_by_name("ctl00$body$txtPassword").send_keys("don@123")
browser.find_element_by_id("body_btnLogin").click()
time.sleep(2)
'click on loans tab'
browser.find_element_by_link_text("Loans").click()

'Drop down'
select1=Select(browser.find_element_by_id("body_cph_Loans_ddlLoanType"))
select1.select_by_visible_text("Personal")
time.sleep(2)
select2=Select(browser.find_element_by_id("body_cph_Loans_ddlLoanName"))
select2.select_by_index(2)
time.sleep(2)
browser.find_element_by_id("body_cph_Loans_txtReqLoanAmount").send_keys("1000000")
browser.find_element_by_id("body_cph_Loans_txtNoOfEMI").send_keys("20")
time.sleep(2)
browser.find_element_by_id("body_cph_Loans_btnViewEMI").click()
time.sleep(2)

'get text'
print("EMI IS "+browser.find_element_by_id("body_cph_Loans_lblEMIAmountText").text)
