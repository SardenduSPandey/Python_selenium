from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

' FRAMES'
 
browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.181.42/Automation/DemoApps/PopUpBox.aspx")
time.sleep(2)
browser.find_element_by_link_text("Frames").click()
time.sleep(1)
 
'move based on index'
browser.switch_to.frame(1)
result=browser.find_element_by_class_name("frames-page").text
print(result)
 
'moving control to parent frame'
browser.switch_to.default_content()
time.sleep(1)
result=browser.find_element_by_class_name("frames-page").text
print(result)


'Mouse Hovering'
browser=webdriver.Chrome(executable_path="D:\\ChromeDriver96.exe")
browser.get("http://10.82.180.36:8080/EDUBank/")
time.sleep(1)
browser.find_element_by_id("userId").send_keys("Steven")
browser.find_element_by_id("password").send_keys("Steven!123")
time.sleep(1)
browser.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]/form/button").click()
time.sleep(1)
result=browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[2]/span").text
print(result)

' logout mouse hovering'
parent=browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/span")
child=browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div/div/p[3]/a")
time.sleep(1)
actions=ActionChains(browser)
actions.move_to_element(parent)
actions.click(child)
actions.perform()

# actions=ActionChains(browser).move_to_element(parent).click(child).perform()









