from selenium import webdriver
import time
import xlrd
from xlwt.Workbook import Workbook
from xlwt.Worksheet import Worksheet
from xlutils.copy import copy
import openpyxl
from selenium.webdriver.support.ui import Select




browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.180.36/Common/Login.aspx")
'login into application'
browser.find_element_by_id("body_txtUserID").send_keys("donhere")
browser.find_element_by_name("ctl00$body$txtPassword").send_keys("don@123")
browser.find_element_by_id("body_btnLogin").click()
time.sleep(2)

'click on loans tab'
browser.find_element_by_id("GeneralTabMenu_Loans_li_Cust").click()

'Excel Automation - Reading Data'
Workbook=xlrd.open_workbook("C:\\Users\\naveenkumar.murugan\\Desktop\\valss.xlsx")
Worksheet=Workbook.sheet_by_index(0)
Writebook=copy(Workbook)
writesheet=Writebook.get_sheet(0)

RowCount=Worksheet.nrows

for i in range(1,RowCount):
    LoanType=Worksheet.cell_value(i,0)
    LoanName=Worksheet.cell_value(i,1)
    LoanAmount=Worksheet.cell_value(i,2)
    Emi=Worksheet.cell_value(i,3)
    
    select1=Select(browser.find_element_by_id("body_cph_Loans_ddlLoanType"))
    select1.select_by_visible_text(LoanType)
    time.sleep(2)
    select2=Select(browser.find_element_by_id("body_cph_Loans_ddlLoanName"))
    select2.select_by_visible_text(LoanName)
    time.sleep(2)
    browser.find_element_by_id("body_cph_Loans_txtReqLoanAmount").send_keys(LoanAmount)
    browser.find_element_by_id("body_cph_Loans_txtNoOfEMI").send_keys(int(Emi))
    time.sleep(2)
    browser.find_element_by_id("body_cph_Loans_btnViewEMI").click()
    time.sleep(2)
    result=browser.find_element_by_id("body_cph_Loans_lblEMIAmountText").text
    print(result)
    
    'write data into excel'
    writesheet.write(i,4,result)
Workbook.save("C:\\Users\\naveenkumar.murugan\\Desktop\\valss.xlsx")





