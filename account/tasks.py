from __future__ import absolute_import, unicode_literals
import random
from celery.decorators import task
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@task(name='sent_registration_email')
def sent_registration_email(sponsor_name, sponsor_email, downliner_name, downliner_email):
    fromaddr = "support@bethemillionaire.com"
    toaddr = sponsor_email

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "Congratulations %s! You have just referred a new member to BeTheMillionaire!" %sponsor_name


    body = """
    <p>Congratulations {}! You have just referred a new member to BeTheMillionaire!</p>
    <p>You’re well on your way to long term Bitcoin riches, keep moving forward!</p>
    <p>Make sure to connect with this person ASAP and help him/her go through the course Secrets To Growing Your Wealth In Bitcoins”, and complete ALL Fast Start steps, get Bitcoin in their wallet and register their accounts in our Wealth Building vehicles under “Passive Profits” tab!</p>
    
    <p>-------------------------------------------------------</p>
    
    <p>Name:  {}</p>
    <p>Email: {}</p>
    
    <p>-------------------------------------------------------</p>
    
    <p>The more referrals you bring to BeTheMillionaire, the more Bitcoins you’ll earn in multiple ways, and you can also win 0.05+ Bitcoins in our weekly competition with prizes, please check the Leaderboards!</p>
    
    <p>Also show your new member the benefits of upgrading to Premium or VIP level coaching program and earn up to 70% commissions!</p>
    
    <p>Here you will find more information on that: https://www.bethemillionaire.com/account/membership-account/membership-levels/</p><br>
    
    <p>As a FREE member you earn 10% commissions on your members upgrades, as a Premium member 40% and as VIP member a whopping 70% commissions!</p>
    
    
    <p>Also make sure there are plugged in to our Official Facebook group!</p>
    <p>Let’s help together a new wave of people become Crypto Millionaires!</p>
    <br>
    <p>Sincerely,</p>
    <p>Mena Refaat & BeTheMillionaire Team</p>
    
    """.format(sponsor_name, downliner_name, downliner_email)

    msg.attach(MIMEText(body, 'html'))


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(fromaddr, "menaKP00")

    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)
    server.quit()



#send registerred email
@task(name='sent_registred_email')
def sent_registred_email(name, email, password):
    fromaddr = "support@bethemillionaire.com"
    toaddr = email

    msg = MIMEMultipart()

    msg['From'] = fromaddr
    msg['To'] = toaddr

    msg['Subject'] = "مرحباً فى مشروع كريبتو مليونير !"


    body = """
    <p>مرحبا</p>
    <p>!مرحبا و شكرا لأنضمامك الى مشروع كريبتو مليونير</p>
    <p>سوف تحصل الان على  تدريب حصرى وتتعلم كيف تستطيع ان تكسب بيتكوين 
بطرق متنوعة, كيف تستخدم السيستم لتكسب دخل متعدد فى اقرب وقت ممكن بداية من       
.اليوم      
    </p>
    
    <p>تستطيع الدخول بهذه المعلومات</p>
    
    <p>-------------------------------------------------------</p>
    
    <p>Username:  {}</p>
    <p>Password: {}</p><br>
    <p>Here is your login link: https://www.bethemillionaire.com/account/login/</p>
    
    <p>-------------------------------------------------------</p>
    
    <p>Please also join our Facebook Group here for updates and support:</p>
    
    <p>https://www.facebook.com/groups/336201610190269/</p>
    
    <p>وابقى متطلعا اولاً بأول بجميع التدريبات الجديدة</p>
    
    <p>.وراسلنى فى أى وقت</p>
    
    
    <p>شكراً</p>
    <p>مينا رفعت</p>
    <p>مؤسس مشروع كريبتو مليونير</p>
    
    """.format(name, password)

    msg.attach(MIMEText(body, 'html'))


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    server.login(fromaddr, "menaKP00")

    text = msg.as_string()

    server.sendmail(fromaddr, toaddr, text)
    server.quit()

