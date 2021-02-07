import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

receiver_list = open("receiver_list.txt", "r")
lists = receiver_list.readlines()
receiver_list.close()

msg = MIMEMultipart()

print("Masukkan :")
sender = str(input("Email pengirim : "))
sender_pasw = str(input("Password pengirim : "))

tittle =  str(input("\nJudul Email : "))
body =  str(input("Isi Email :\n"))

def sendMail(sender,sender_pasw,receiver,subject,body,nameFile,directory):
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    filename = nameFile
    attachment = open(directory, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, sender_pasw)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

try:
    for x in lists:
        sendMail(sender,sender_pasw,x,tittle,body,"python.png","python.png")
    print("Sukses!")
except:
    print("Gagal!")

# Referensi:
# https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
# https://saktidwicahyono.name/2011/04/25/kirim-email-via-gmail-menggunakan-python/
# https://www.pythonindo.com/cara-mengirim-email-menggunakan-python/