import smtplib  #inbuilt Service to connect to smtp server

to = input("Enter the email:\n ")

content = input("Enter the content for mail")

def send_mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("senderemail@gmail.com", '12345')
    server.sendmail('sendermail@gmail.com', to, content)
    server.close()

send_mail(to, content)
