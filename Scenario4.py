from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.181.42/Automation/DemoApps/PopUpBox.aspx")

'accept alert box'
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/input").click()
time.sleep(2)
obj=browser.switch_to.alert
obj.accept()
 
'decline alert box'
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/input").click()
time.sleep(2)
obj.dismiss()
 
'send keys alert'
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/input").click()
time.sleep(2)
obj.send_keys("Naveenkumar Murugan")
obj.accept()

'Drag and drop'
browser.find_element_by_link_text("Drag 'N' Drop").click()
source=browser.find_element_by_id("draggable")
destination=browser.find_element_by_id("droppable")
mouse=ActionChains(browser).drag_and_drop(source, destination)
mouse.perform()