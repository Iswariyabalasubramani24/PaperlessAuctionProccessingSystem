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
    if(userrole=="ROLE_01"):
          watchedid=form.getvalue('ID')
          query="delete from watchlist where ID='%s'"%(watchedid)
          res=cursor.execute(query)
          if(res==1):
              db.commit()
              print("<script>alert('Deleted');location.href='b-watch-page.py';</script>")
          else:
              db.rollback()
              print("<script>alert('Error in Deleting');location.href='b-watch-page.py';</script>")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")          
    
