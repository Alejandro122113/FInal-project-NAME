# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:22:08 2022

@author: edgar
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = 'C:/Users/Edgar/Desktop/chromedriver.exe')
driver.get("https://excelacademy.powerschool.com/public/home.html")
time.sleep(2)

def login(username,password):
    loginuser = driver.find_element_by_id('fieldAccount')
    loginuser.send_keys(username)
    
    time.sleep(2)
    
    loginpass = driver.find_element_by_id('fieldPassword')
    loginpass.send_keys(password)
    loginpass.send_keys(Keys.RETURN)
    time.sleep(2)
    
    
login('edgar.solis', 'Excel3819')

APUSH = {"CW": [], "HW": [], "EX": [], "Quizzes": []}

HP = {"Participation": [], "HW": [], "Projects": [], "IA": []}


for i in APUSH.keys():
    avg = sum(APUSH[i]) 
    if i == "CW":
        USHTotal1 = APUSH[i] / 0.2
    elif i == "HW":
        USHTotal2 = APUSH[i] * 0.3 
    elif i == "EX":
        USHTotal3 = APUSH[i] * 0.1
    elif i == "Quizzes":
        USHTotal4 = APUSH[i] * 0.4

        
for i in HP.keys():
    pythonGrade = driver.find_element_by_xpath("/html/body/div[2]/div[4]/div[2]/div[3]/div/table[1]/tbody/tr[4]/td[14]/a")
    q2Grade = pythonGrade.get_attribute('text')
    pythonGrade.click()
    time.sleep(1)
    #make a new tab
    driver.execute_script("window.open('about:blank','secondtab');")
    driver.switch_to.window("secondtab")
    time.sleep(1)
    #load powerschool
    driver.get("https://excelacademy.powerschool.com/guardian/home.html")
    time.sleep(2)
    avg = sum(HP[i]) 
    if i == "Participation":
        HPTotal1 = HP[i] / 0.15
    elif i == "HW":
        HPTotal2 = HP[i] / 0.3
    else:
        HPTotal3 = HP[i] / 0.4
    
        
        