from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.keralapsc.gov.in/answerkey_omrexams')
lk=driver.find_elements(By.XPATH,"//table[@class='cols-6']/tbody/tr/td[1]/a")
for i in lk:
    print(i.get_attribute('href'))
mk=driver.find_element(By.XPATH,"//table[@class='cols-6']/tbody/tr[1]/td[1]/a[1]").click()
print(mk)
