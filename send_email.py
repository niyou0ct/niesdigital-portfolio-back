from email.mime.text import MIMEText
import smtplib, ssl

account = 'yuki.niiuchi@niesdigital.com'
password = 'Yn170409'

to_email = account
from_email = 'axaebyxo11@gmail.com'

subject = 'テストメール'
message = 'テストメール'
msg = MIMEText(message, 'html')
msg['Subject'] = subject
msg['To'] = to_email
msg['From'] = from_email

# server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context = ssl.create_default_context())
server = smtplib.SMTP('smtp.gmail.com', 465)
server.login(account, password)
server.send_message(msg)
server.quit()
