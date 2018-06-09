import requests
import pymysql


def send_simple_message(receiver):
    html = """
    
    
    <html>
      <head></head>
      <body>
        
        hi,<br>
        
        welcome to BeTheMillionaire.<br>
        
        BeTheMillionaire is update profile section for you.<br>
        
        you can change your profile information, account password, add your affiliate link and change your password.<br>
        
        you can simply login to BeTheMillionaire by following the link:<br>
        
        https://www.bethemillionaire.com/account/login/<br>
        
        then you click "my profile setting" under menu "my account".<br>
        
        or click here after login:
        <br>
        https://www.bethemillionaire.com/account/membership-account/profile/
        <br><br>
        
        
        thanks<br>
        BeTheMillionaire Team<br>       
                  
                
      </body>
    </html>
    
    
    
    """


    return requests.post(
        "https://api.mailgun.net/v3/bethemillionaire.com/messages",
        auth=("api", "8e2ff957f5281ca176f75e1089eb2af9-b892f62e-fcfd83f3"),
        data={"from": "live@bethemillionaire.com",
              "to": receiver,
              "subject": "Important notice from BeTheMillionaire",
              "html": html})



def email_list_from_db():
    db = pymysql.connect(user="root",passwd="Nstu12345678~!",host="46.101.14.199",db="be_themillionaire")
    cursor = db.cursor()
    cursor.execute("SELECT email from account_userprofile")
    data=cursor.fetchall()
    email_list = []

    for row in data :
        email_list.append(row[0])
    db.close()

    return email_list




def email_trigger():
    email_list = email_list_from_db()

    n=1
    for email in email_list:
        send_simple_message(email)
        print("%d. email send to %s" %(n, email))

        n += 1



if __name__ == '__main__':
    email_trigger()



