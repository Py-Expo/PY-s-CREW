import pandas as pd
from datetime import datetime,date
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

df = pd.read_excel("New Microsoft Excel Worksheet.xlsx")

df['CREATION DATE'] = pd.to_datetime(df['CREATION DATE'], format='% `d/%m/%Y')
df['EXPIRY DATE'] = pd.to_datetime(df['EXPIRY DATE'], format='%d/%m/%Y')

today = pd.Timestamp.now().normalize()

expired_data = df[df['EXPIRY DATE'].dt.normalize() <= today]

with pd.ExcelWriter("New Microsoft Excel Worksheet.xlsx", engine="openpyxl",mode='a') as writer:

   DF1= expired_data.to_excel(writer, index=False, sheet_name="expiry_date")
   df_sheet2 = pd.read_excel('New Microsoft Excel Worksheet.xlsx', sheet_name='expiry_date')

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


