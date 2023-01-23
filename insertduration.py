#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-type:text/html\r\n\r\n")
import os
import pymysql
import cgi
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
    if(userrole=="ROLE_03"):
        form=cgi.FieldStorage()
        duration=form.getvalue("duration-length")
        query="select ifnull(max(sno),0) from duration"
        cursor.execute(query)
        result=cursor.fetchone()
        prefix="DURA_"
        postfix=result[0]+1
        durationid=prefix+str(postfix)

        equery="select * from duration where duration='%s'"%(duration)
        if(cursor.execute(equery)>0):
            print("<script>alert('Already Exists');location.href='upload-duration.py';</script>")
        else:
            iquery="insert into duration(id_duration,duration) values('%s','%s')"%(durationid,duration)
            res=cursor.execute(iquery)
            if(res==1):
                db.commit()
                print("<script>alert('Inserted');location.href='upload-duration.py';</script>")
            else:
                db.rollback()
                print("<script>alert('Error in Inserting');location.href='upload-duration.py';</script>")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")

