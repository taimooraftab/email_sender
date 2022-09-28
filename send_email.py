import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()


email['from'] = 'Taimoor Aftab'
email['to'] = 'taimooraftab@ymail.com'
email['subject'] = 'You won 1,000,000 dollars'

email.set_content(html.substitute({'name':'TinTin'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('taimooraftab95@gmail.com','gusf llec jjuy mhal')
	smtp.send_message(email)
	print('all good boss!')