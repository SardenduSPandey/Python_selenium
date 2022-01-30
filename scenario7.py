from selenium import webdriver
import time
import xlwt
from xlwt.Workbook import Workbook
from xlwt.Worksheet import Worksheet
from xlutils.copy import copy


browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.180.36/Common/Login.aspx")
'login into application'
browser.find_element_by_id("body_txtUserID").send_keys("donhere")
browser.find_element_by_name("ctl00$body$txtPassword").send_keys("don@123")
browser.find_element_by_id("body_btnLogin").click()
time.sleep(2)

'Excel automation write into new excel sheet .xlx format'

table=browser.find_element_by_id("body_cph_MyAccount_gvAccountDetails")
rows=table.find_elements_by_tag_name("tr")
book = xlwt.Workbook()
sheet=book.add_sheet("Account Details", False)

for i in range(0, len(rows)):
    col=rows[i].find_elements_by_tag_name("td")
    for j in range(0,len(col)):
        if(j==0):
            accountno=col[j].text
            sheet.write(i,0,accountno)
        elif(j==2):
            balance=col[j].text
            sheet.write(i,2,balance)
        else:
            continue
        
book.save("C:\\Users\\naveenkumar.murugan\\Desktop\\newbook.xls")




