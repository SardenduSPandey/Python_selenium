from selenium import webdriver
import time


browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.180.36/Common/Login.aspx")
'login into application'
browser.find_element_by_id("body_txtUserID").send_keys("donhere")
browser.find_element_by_name("ctl00$body$txtPassword").send_keys("don@123")
browser.find_element_by_id("body_btnLogin").click()
time.sleep(2)

'webtable iteration'
table=browser.find_element_by_id("body_cph_MyAccount_gvAccountDetails")
rows=table.find_elements_by_tag_name("tr")
time.sleep(2)
for i in range(0,len(rows)):
    if(i!=0):
        cols=rows[i].find_elements_by_tag_name("td")
        for j in cols:
            if(len(cols)>3):
                if(cols[3].text=="FD"):
                    print(cols[1].text)
                    break

'screenshot'
browser.get_screenshot_as_file("D:\\image1.png")