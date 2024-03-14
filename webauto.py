from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the chromedriver executable
driver_path = 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs'

options = Options()

# If you want to suppress browser notifications, add this line
# options.add_argument('--disable-notifications')
capabilities = {
    'browserName': 'chrome',
    'version': '',
    'platform': 'ANY',
    'javascriptEnabled': True
}
# If you want to run headless (without opening the browser window), add this line
# options.add_argument('--headless')

# Initialize a webdriver instance for Chrome with options
driver = webdriver.Chrome(executable_path=driver_path, options=options,desired_capabilities=capabilities)

# Navigate to the URL
driver.get("https://archive.data.gov.my/data/en_US/dataset/msc-malaysia-cybercentre-and-cybercity")

# Find the element you want to click by class name
element_class_name =    
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, element_class_name)))

# Click the element
element.click()

# After you're done, close the browser
driver.quit()
