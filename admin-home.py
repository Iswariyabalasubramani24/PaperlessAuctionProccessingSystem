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
    if(userrole=="ROLE_03"):
            print("""<html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Admin Home</title>
            <link href="css/bootstrap.min.css" rel="stylesheet">
            <meta charset='UTF-8'>

            <style class="cp-pen-styles">body {
            background-color: #f3f5f7;
            font-family: 'Helvetica Neue', Arial, sans-serif;
                }

                .card {
            background-color: #fff;
            box-shadow: 0 0 6px rgba(0, 0, 0, 0.1);
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            max-width: 300px;
            height: 375px;
            border-radius: 10px;
            overflow: hidden;
                }

                .card .about {
            height: 225px;
            padding: 20px;
            box-sizing: border-box;
                }

                .card .about h3,
                .card .about .lead {
                font-weight: 300;
                margin: 0;
            }

                .card .about h3 {
                font-size: 24px;
                }

                .card .info p {
                font-size: 11px;
                color: #aaa;
                font-weight: 300;
                }

            </style>
        </head>

            <!--List of auctions, items, users. Analytics.-->


<body>

<div class="card" style="height:auto; width:auto;">
    <div class="col-sm-12" style="height:auto; width:auto;">
        <!-- Custom information -->
        <div class="about" style="height:auto; width:auto;">
            <img class="card-img-top" src="efast.png" alt="Card image">
            <div class="spacer" style="height:20px"></div>
            <h3>Welcome to the Administrator's Home</h3>

            <div class="spacer" style="height:30px"></div>
            <div class="btn-group-vertical btn-block ">
                <button type="button" class="btn btn-primary" onclick="window.location='./upload-category.py';">Add new Category</button>
                <div class="spacer" style="height:5px"></div>
                <button type="button" class="btn btn-primary" onclick="window.location='./upload-duration.py';">Add new Duration</button>
                <div class="spacer" style="height:5px"></div>
                <button type="button" class="btn btn-primary" onclick="window.location='./auctions.py';">Inspect all Auctions</button>
                <div class="spacer" style="height:5px"></div>
                <button type="button" class="btn btn-primary" onclick="window.location='./users.py';">Inspect all users</button>
                <div class="spacer" style="height:30px"></div>
                <button type="button" onclick="window.location='adminlogout.py'" class="btn btn-default">Logout</button>

            </div>
            <div class="spacer" style="height:20px"></div>

        </div>
    </div>
</div>
</body>
</html>""")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
