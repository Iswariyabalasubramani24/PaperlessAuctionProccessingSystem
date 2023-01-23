#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-Type:text/html\n\r")
import os
import pymysql
import cgi
form=cgi.FieldStorage()
db=pymysql.connect(user="root",password="root",host="localhost",database="onlineauction")
if db:
    cursor=db.cursor()
    sql="select * from tbl_session"
    userid=""
    useremail=""
    userrole=""
    if(cursor.execute(sql)>0):
        results=cursor.fetchall()
        for row in results:
            userid=row[0]
            useremail=row[1]
            userrole=row[2]
    if(userrole=="ROLE_02"):
          auctionid=form.getvalue('aid')
          query="delete from auction where ID_AUCTION='%s'"%(auctionid)
          res=cursor.execute(query)
          if(res==1):
              db.commit()
              print("<script>alert('Deleted');location.href='s-myprofile.py';</script>")
          else:
              db.rollback()
              print("<script>alert('Error in Deleting');location.href='s-myprofile.py';</script>")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")          
    
