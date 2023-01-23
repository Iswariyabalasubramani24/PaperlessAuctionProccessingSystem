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
        print("""
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>All Users</title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/profile.css" rel="stylesheet">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <style>
            .checked {
            color: orange;
            }
        </style>
        </head>
        <body>
        <!-- nav bar -->
        <nav class="navbar navbar-light bg-light">
        <a class="navbar-brand">
            <img src="eFast.png" width="100" height="30" alt="">
        </a>
        </nav>
        <!-- Bid history -->
        <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>
        <div class="container">
        <button type="button" class="btn btn-default btn-sm" onclick="window.location='./admin-home.py';"><i class="glyphicon glyphicon-arrow-left"></i> Back to Home</button>
        <div class="row">
        <div class="col-md-12">
        <h2>All Buyers</h2>
        <hr/>
        <div class="table-responsive">
        <table id="mytable" class="table table-bordred table-striped">
        <thead>
        <th>ID User</th>
        <th>First Name</th>
        <th>Last Name</th>
        <th>Number of bids made</th>
        </thead>
        <tbody>""")
        sqlquery= "SELECT ID_USER, FNAME, LNAME FROM user WHERE ID_ROLE = 'ROLE_01'"
        cursor.execute(sqlquery)
        result=cursor.fetchall()
        for row in result:
            currentuser =row[0]
            fname = row[1]
            lname = row[2]
            sqlquery1 = "SELECT COUNT(ID_BUYER) as HELLO FROM bid WHERE ID_BUYER ='%s'"%(currentuser)
            cursor.execute(sqlquery1)
            result1=cursor.fetchone()
            count=result1[0]
            print("<tr>")
            print("<td><a href=profile-other.py?uID='%s'>%s</a></td>"%(currentuser,currentuser))
            print("<td>%s</td>"%(fname))
            print("<td>%s</td>"%(lname))
            print("<td>%s</td>"%(count))
            print("</tr>")
        print("""</tbody>
            </table>
            </div>
            </div>
            <div class="col-md-12">
            <h2>All Sellers</h2>
            <hr/>
            <div class="table-responsive">
            <table id="mytable" class="table table-bordred table-striped">
            <thead>
            <th>ID User</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Number of auctions created</th>
            </thead>
            <tbody>""")
        squery= "SELECT ID_USER, FNAME, LNAME FROM user WHERE ID_ROLE ='ROLE_02'"
        cursor.execute(squery)
        result2=cursor.fetchall()
        for row in result2:
            userID = row[0]
            fname = row[1]
            lname = row[2]
            squery1="SELECT COUNT(ID_SELLER) as HI FROM auction WHERE ID_SELLER='%s'"%(userID)
            cursor.execute(squery1)
            result3=cursor.fetchone()
            scount =result3[0]
            print("<tr>")
            print("<td><a href=profile-other.py?uID='%s'>%s</a></td>"%(userID,userID))
            print("<td>%s</td>"%(fname))
            print("<td>%s</td>"%(lname))
            print("<td>%s</td>"%(scount))
            print("</tr>")
         
            print("""</tbody>
             </table>
             </div>
             </div>
             </div>
             </body>
             </html>""")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
