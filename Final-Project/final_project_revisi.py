# Source : 
#     - https://www.youtube.com/watch?v=sXjpkcF7rPQ
#     - https://code.tutsplus.com/tutorials/sending-emails-in-python-with-smtp--cms-29975

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

file = open('e:\Indonesian AI\Basic-python-b3\Final-project/receiver_list.txt', 'r').read()
flx = file.split()

sender_email = "senjacakraningrat@gmail.com"
rec_email = flx
body = "Hello, this was sent using Python"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(flx)
msg['Subject'] = 'TEST SUBJECT'

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

password = input(str("Masukan Password :"))
server.login(sender_email, password)
print("Login success!")
server.sendmail(sender_email, rec_email, text)
server.quit()

print("Email has been sent to ", rec_email)