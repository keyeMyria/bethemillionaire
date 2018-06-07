import pymysql


x = pymysql.connect("46.101.14.199","root","Nstu12345678~!","be_themillionaire")


if x:
    cursor = x.cursor()
    sql = "select * from account_userprofile"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Fetch all the rows in a list of lists.
        results = cursor.fetchall()
        i=1
        for result in results:
            email = result[5]

            print(i, email)
            i += 1
    except:
        print ("Error: unable to fetch data")

else:
    print('no')
