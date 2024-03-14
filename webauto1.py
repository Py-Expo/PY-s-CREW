import webbrowser
import pandas as pd
from datetime import datetime,date
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


webbrowser.open("https://archive.data.gov.my/data/en_US/dataset/msc-malaysia-cybercentre-and-cybercity"
)

driver_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

driver = webdriver.Chrome(executable_path=driver_path)


driver.get("https://archive.data.gov.my/data/en_US/dataset/msc-malaysia-cybercentre-and-cybercity")

element_class_name = "float-right btn btn-primary btn-lg"


element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, element_class_name)))


element.click()


driver.quit()

df = pd.read_excel("New Microsoft Excel Worksheet.xlsx")



today = pd.Timestamp.now().normalize()

expired_data = df[df['Sheet1'].dt.normalize() <= today]

with pd.ExcelWriter("MSC Malaysia Cybercentre and Cybercity.xlsx", engine="openpyxl",mode='a') as writer:

   DF1= expired_data.to_excel(writer, index=False, sheet_name="Sheet1")
   df_sheet2 = pd.read_excel("MSC Malaysia Cybercentre and Cybercity.xlsx", sheet_name='Sheet1')

print( df )



sender_email = "aj3681528@gmail.com"
receiver_email = "srimathii1231@gmail.com"
password = "rhvlnsuukkugeook"


message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Subject of the Email"

body = "This is the body of the email."
message.attach(MIMEText(body, "plain"))

with smtplib.SMTP("smtp.example.com", 587) as server:
   
    server.starttls()

    
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email sent successfully!")


