from email.mime.text import MIMEText
import smtplib

account = 'yuki.niiuchi@niesdigital.com'
password = 'Yn170409'

to_email = account
from_email = ''

subject = 'テストメール'
message = 'テストメール'
msg = MIMEText(message, 'html')
msg['To'] = to_email
msg['From'] = from_email

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(account, password)
server.send_message(msg)
server.quit()