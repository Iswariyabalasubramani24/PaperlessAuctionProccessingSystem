#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-Type:text/html\n\r")

import cgi
import pymysql
form=cgi.FieldStorage()
if(form.getvalue('submit')=="Register"):
    
    firstname=form.getvalue('firstname')
    lastname=form.getvalue('lastname')
    email=form.getvalue('email')
    role=form.getvalue('radio')
    password=form.getvalue('password')
    rpassword=form.getvalue('password-repeat')
    if(password==rpassword):
        
        db=pymysql.connect(user="root",password="root",host="localhost",database="onlineauction")

        if(db):
            cursor=db.cursor()
            iquery="select ifnull(max(id),0) from user";
            cursor.execute(iquery)
            result=cursor.fetchone()
            prefix="USER0"
            postfix=result[0]+1
            userid=prefix+str(postfix)
            query="select * from user where email='%s' and id_role='%s'"%(email,role)
            if(cursor.execute(query)>0):
                print('<script>alert("Already Exists");location.href="register.py";</script>')
            else:
                sql="insert into user(id_user,fname,lname,email,pass,id_role) values('%s','%s','%s','%s','%s','%s')"%(userid,firstname,lastname,email,password,role)
                res=cursor.execute(sql)
                if(res==1):
                    db.commit()
                    print('<script>alert("Registered Successfully"); location.href = "login.py"; </script>')
                else:
                    db.rollback()
        else:
            print("Db is Not Connected")
    else:
        print('Password Do not match')
