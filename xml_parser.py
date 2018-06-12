import requests
import pymysql
from xml.etree import ElementTree as ET



def parse_db_and_insert():
    db = pymysql.connect(user="root",passwd="root",host="localhost",db="fivrr")
    cursor = db.cursor()

    cursor.execute("select id, url from processing where tinyurl is NULL")
    data=cursor.fetchall()

    for row in data :
        id = row[0]
        url = row[1]

        xml_content = api_call(url)

        try:
            cursor.execute("""UPDATE processing SET tinyurl=%s WHERE id=%s""",(xml_content, id))
            db.commit()
            print('inserted', xml_content)
        except:
            db.rollback()


    db.close()


def api_call(url):
    url = 'http://5m5.link/yourls-api.php?username=username&password=password&action=shorturl&url={}'.format(url)
    response = requests.get(url)

    xml_content = response.content

    root = ET.fromstring(xml_content)

    tinyurl = False
    for child in root.iter('shorturl'):
        tinyurl = ET.tostring(child, method="text").strip().decode('utf-8')

    return tinyurl



parse_db_and_insert()



