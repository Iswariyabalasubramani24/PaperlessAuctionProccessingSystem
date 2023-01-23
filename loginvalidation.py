#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-Type:text/html\n\r")
import cgi
import pymysql
form=cgi.FieldStorage()
if(form.getvalue('submit')=="Login"):
    email=form.getvalue('email')
    password=form.getvalue('password')
    db=pymysql.connect(user="root",password="root",host="localhost",database="onlineauction")
    if(db):
        cursor=db.cursor()
        sql="select * from user where email='%s' and pass='%s'"%(email,password)
        #print(sql)
        if(cursor.execute(sql)>0):
            result=cursor.fetchone()
            userid=result[0]
            fname=result[1]
            lname=result[2]
            email=result[3]
            password=result[4]
            idrole=result[5]
            
            

##            // if valid
##            $_SESSION['userID'] = $userID;
##            $_SESSION['username'] = $email;
##            $_SESSION['first_name'] = $first_name;
##            $_SESSION['last_name'] = $last_name;
##            $_SESSION['role'] = $role;
##
##
##            setcookie('userID', $userID,   time() + (60 * 60 * 24 * 30));
##            setcookie('username', $email,  time() + (60 * 60 * 24 * 30));
##            setcookie('first_name', $first_name,  time() + (60 * 60 * 24 * 30));
##            setcookie('last_name', $last_name,  time() + (60 * 60 * 24 * 30));
##            setcookie('role', $role,  time() + (60 * 60 * 24 * 30));


            insertquery="insert into tbl_session values('%s','%s','%s')"%(userid,email,idrole)
            res=cursor.execute(insertquery)
            if(res==1):
                db.commit()
                if(idrole=='ROLE_01'):
                    print('<script>alert("Login is Success");location.href="b-home.py";</script>')
                elif(idrole=='ROLE_02'):
                    print('<script>alert("Login is Success");location.href="s-home.py";</script>')
                elif(idrole=='ROLE_03'):
                    print('<script>alert("Login is Success");location.href="admin-home.py";</script>')
                else:
                    print("<div align=center><p><strong>Please Enter A Valid USerName and Password</strong></p></div>")
            
            else:
                print("<div align=center><p><strong>Error in Inserting into Session</strong></p></div>")
            
        else:
            print("<div align=center><p><strong>Please Enter A Valid USerName and Password</strong></p></div>")
    else:
        print("DB is Not Connected")
