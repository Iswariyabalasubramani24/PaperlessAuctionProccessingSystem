#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-type:text/html\r\n\r\n")
import os
import pymysql
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
        print("""
        
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>Seller Home</title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <script src="js/jquery.js"></script>
        <script src="js/bootstrap.bundle.js"></script>
        </head>
        <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="s-home.py">
        <img width="100" src="efast.png">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
        aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse">
        <ul class="navbar-nav ml-auto">
        <li><a href="s-myprofile.py"><img height="30px" src="img/user1.png">""")
        print("<br>%s"%(userid))
        print("""<?php echo "Hi "; echo  $_SESSION['first_name'] ; echo " "; echo   $_SESSION['last_name'] ;   ?>  </a></li>
        </ul>
        </div>
        <button style="margin-left: 10px" type="button" onclick="window.location='sellerlogout.py';" class="btn btn-outline-danger btn-sm ">Logout</button>
        </nav>
        <br><br>
        <div class="container">
        <h1>Seller Hub</h1>
        </div>
        <br>
        <!--MAIN BODY OF THE PAGE-->

        <div class="container-fluid">
        <div style="width: 82%; margin: 0 auto; float: none; margin-bottom: 20px; ">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">CREATE AN AUCTION</h5>
        <p class="card-text">Create an auction based on an item to list it!</p>
        <a href="createAuction.py" class="btn btn-primary">Create a new auction</a>
        <img src="https://media.giphy.com/media/E9k0HTREY1qJW/giphy.gif" alt="" style="width:48px;height:48px;">
        </div>
        </div>
        <div id="spacer" style="height: 10px;"> </div>
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">View your profile and the items report</h5>
        <p class="card-text">Account information, your rating, feedback and viewing traffic of items</p>
        <a href="s-myprofile.py" class="btn btn-primary">Go to your profile page</a>
        <img src="https://media.giphy.com/media/13C8OJmeUxGz4Y/source.gif" alt="" style="width:48px;height:48px;">
        <img src="https://cdn.dribbble.com/users/870415/screenshots/2746862/linegraph.gif" alt="" style="width:48px;height:48px;">
        </div>
        </div>
        </div>
        </div>
        </body>
        </html>""")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")

