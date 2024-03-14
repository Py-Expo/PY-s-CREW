import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC








driver_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

driver = webdriver.Chrome(driver_path)

driver.get('https://archive.data.gov.my/data/en_US/dataset/msc-malaysia-cybercentre-and-cybercity')

element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME,"float-right btn btn-primary btn-lg")))

button.click()

driver.quit()
