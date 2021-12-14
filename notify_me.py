import time
import smtplib
import requests
import mimetypes
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from bs4 import BeautifulSoup


def send_mail():
    
    mail_subject = "[SUBJECT]" # MAIL SUBJECT

    # A MESSAGE TO NOTIFY YOU IF THE ITEM IS AVAILABLE
    # EXAMPLE:
    mail_content = """
    HARRY UP BUY THE ITEM [URL]
    """

    #The mail addresses and password
    sender_address = '[GMAIL EMAIL]'
    sender_pass = "[GMAIL PASSWORD]"

    # reciever mail will be gotten from the file and passed as function argument
    receiver_address = "[RECEIVER EMAIL]" 

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = mail_subject   # The subject line CHANGE THIS IF YOU NEED

    #The body for the mail
    message.attach(MIMEText(mail_content, 'plain'))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls() # enable tls security
    session.login(sender_address, sender_pass)  #login with mail and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print("[*] Mail Sent")
    exit()


while(True):
  url="[URL]"
  response = requests.get(url)


  # HERE YOU NEED TO FIND A WAY TO GET SPECIAL PART OF A PAGE
  # FOR EXAMPLE:
  # I WANT TO SEE IF THERE IS A 'span' TAG WITH 'not-available' CLASS
  soup = BeautifulSoup(response.content,'html.parser')
  spans = soup.find_all('span',"not-available")
  
  # IF NOT AVAILABLE
  if spans:
    print("[-] Not Avaliable!")

  # Avaliable
  else:
    print("[+] Avaliable")
    send_mail() # SEND EMAIL
    exit() # EXIT

  
  time.sleep(300) # Refresh every 5 minutes 

  '''
  1. click Win+R

  2. type shell:startup

  3. drag and drop your python file my_script.py
        if you don't need the console: change extension from my_script.py to my_script.pyw
        else: create run_my_script.cmd with content: python path\to/\your\my_script.py


  '''