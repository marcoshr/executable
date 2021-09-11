"""
FOLLOWING THIS TUTORIAL:
https://stackoverflow.com/questions/10147455/how-to-send-an-email-with-gmail-as-provider-using-python

"""
    
import smtplib
fromaddr = 'marcoshernandezhr@gmail.com'
toaddrs  = 'marcoshernandezhr@gmail.com'
msg = 'exitooooooooo'

username = 'marcoshernandezhr@gmail.com'
password = 'Lost4815162342'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)

server.sendmail(fromaddr, toaddrs, msg)

server.quit()