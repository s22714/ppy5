import zad5 as z5
import smtplib
from email.mime.text import MIMEText
def send_email(users):
    for user in users:
        recipient = user["email"]
        subject = "Grade"
        grade = user["ocena"]
        body = f"Your grade: {grade}"
        sender = ""
        password = ""

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipient, msg.as_string())
        smtp_server.quit()
        user["status"] = "MAILED"
    z5.zapisz_w_pliku(users, "stud.txt")
    return users