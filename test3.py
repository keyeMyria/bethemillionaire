import requests
import pymysql
from xml.etree import ElementTree as ET



def fetchdb():
    db = pymysql.connect(user="root",passwd="root",host="localhost",db="fivrr")
    cursor = db.cursor()

    cursor.execute("select id, tinyurl, url from processing")
    data=cursor.fetchall()

    for row in data :
        id = row[0]
        tinyurl = row[1]
        url = row[2]

        print(tinyurl)

    db.close()

fetchdb()
