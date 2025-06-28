import os,smtplib,glob,ssl
from email.message import EmailMessage

password=os.getenv("pp")
sender_email=os.getenv("smail")
receiver_email=os.getenv("rmail")


msg=EmailMessage()
msg["From"]=sender_email
msg["To"]=receiver_email
msg["Subject"]="Stock data"

csv_files=glob.glob("*.csv")
if not csv_files:
    msg.set_content("No csv files were present to attach.Likely failure happened")
else:
    for file in csv_files:
        with open(file,"rb") as f:
            msg.add_attachment(f.read(),maintype="text",subtype="csv",filename=os.path.basename(f.name))
if not all([password, sender_email, receiver_email]):
    raise ValueError("One or more required environment variables are missing (pp, smail, remail).")

context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(sender_email,password)
    smtp.send_message(msg)

print("Mail Sent")

for file in csv_files:
    os.remove(file)
