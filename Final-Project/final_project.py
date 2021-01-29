# Source : 
#     - https://www.youtube.com/watch?v=sXjpkcF7rPQ

import smtplib

sender_email = "senjacakraningrat@gmail.com"
rec_email = ["clazzica.zhivella@gmail.com", "winonalestrange@gmail.com"]
password = input(str("Please enter your password : "))
message = "Hey, this was sent using Python."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success!")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)