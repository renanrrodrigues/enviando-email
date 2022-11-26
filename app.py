

import datetime
from email.headerregistry import Address
from email.message import EmailMessage
import smtplib
import time


class SendMail:
    def __init__(self, to, subject, message, email_address=None, email_password=None):
        self.to = to
        self.subject = subject
        self.message = message
        self.email_address = email_address
        self.email_password = email_password
    
    def send_mail(self):
        try:
            
            if self.email_address is None or self.email_password is None:
                print("Did you set email address and password correctly?")
                return False
            
            # create email
            msg = EmailMessage()
            msg['Subject'] = self.subject
            msg['From'] = Address(display_name="⛔ RPA-PIPEFY ⛔", addr_spec=self.email_address) #self.email_address
            msg['To'] = self.to
            msg.set_content(self.message)
            
            # send email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(self.email_address, self.email_password)
                smtp.send_message(msg)
            return True
        
        except Exception as e:
            print("Problem during send email")
            print(str(e))
            return False






email = 'meuEmail@gmail.com'
pw = 'SENHA' # senha antiga 'garzifisti@gufum.com'

para = 'alguem@gmail.com'
assunto = f'🚨 RELATÓRIO COM FALHA!! 🚨 - {datetime.date.today()} '
mensagem = '.....erro no relatório....'

for x in range(1, 10+1):
    SendMail(para, f'{assunto} -> {x}', mensagem, email, pw).send_mail()
    print(f'email enviado. {x}')