import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def sent_commission_email(user, referral, membership, payment_received):
    fromaddr = "support@bethemillionaire.com"
    toaddr = user.email

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "Congratulations %s! You have a referral sale and you got %f!" %(user.username, payment_received)


    body = """
    Congratulation {}, you have a referral sale and you got {}$. We immediately send this payment to your account.<br>
    If you not setup your receiving payment account, please add your receiving payment account in this link:<br>
    https://www.bethemillionaire.com/member-home/payment-account-setting/   <br>
    <br><br>
    
    You get this commission from {}. He just update his membership to {}.<br><br>
    
    Thanks<br>
    Mena Refeat and BeTheMillionaire Team
    """.format(user.username, payment_received, referral.username, membership.name)

    msg.attach(MIMEText(body, 'html'))


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(fromaddr, "menaKP00")

    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)
    server.quit()



def sent_commission_email_confirmation(user, referral, membership, payment_received):
    fromaddr = "support@bethemillionaire.com"
    toaddr = user.email

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "Congratulations %s! We just sent you %.4f!" %(user.username, payment_received)


    body = """
    Congratulation {}, we just sent you {}$.<br>
    <br><br>
    
    You get this commission from {}. He just update his membership to {}.<br><br>
    
    Thanks<br>
    Mena Refeat and BeTheMillionaire Team
    """.format(user.username, payment_received, referral.username, membership.name)

    msg.attach(MIMEText(body, 'html'))


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(fromaddr, "menaKP00")

    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)
    server.quit()
