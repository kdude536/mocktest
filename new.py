import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.keralapsc.gov.in/answerkey_omrexams')
lk=driver.find_elements(By.XPATH,"//table[@class='cols-6']/tbody/tr/td[1]/a")
for i in lk:
    print(i.get_attribute('href'))
driver.find_element(By.XPATH,"//table[@class='cols-6']/tbody/tr[2]/td[1]/a[1]").click()
print(driver.title)
pdf_url=driver.find_element(By.XPATH,"//div[@class='field field--name-field-omr-question-paper field--type-file field--label-above']//a")
link_pdf=pdf_url.get_attribute("href")
print(link_pdf)
res = requests.get(link_pdf)
with open("C:\\Users\\Admin\\Desktop\\xy.pdf","wb") as file:
    file.write(res.content)
pdf_url.click()
time.sleep(3)