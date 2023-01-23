#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
db=pymysql.connect(user="root",password="root",host="localhost",database="onlineauction")
if(db):
    cursor=db.cursor()
    sql="select * from user where email='%s' and pass='%s'"%(email,password)
