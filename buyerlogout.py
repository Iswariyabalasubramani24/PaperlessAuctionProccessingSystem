#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-type:text/html\r\n\r\n")
import os
import pymysql
db=pymysql.connect(user="root",password="root",host="localhost",database="onlineauction")
if db:
    cursor=db.cursor()
    query="delete from tbl_session where userrole='ROLE_01'"
    cursor.execute(query)
    db.commit()
    print("<script>alert('Buyer Logged Out');location.href='index.py';</script>")
else:
    print("not connected")
