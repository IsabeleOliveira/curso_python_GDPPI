from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib


email = 'beleoliveirals4@gmail.com'
senha = 'IS@BELE07'


with open('temp.html', 'r') as html:
    temp = Template(html.read())
    data = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = temp.substitute(nome='Isabele Oliveira', data=data)


msg = MIMEMultipart()
msg['from'] = 'Isabele Oliveira'
msg['to'] = email
msg['subject'] = 'Atenção: este é um e-mail de testes'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with open('Design sem nome.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(email, senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)



