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
        <title>Auction List</title>
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
                <h2>All Auctions</h2>
                <hr/>
                <div class="table-responsive">
                <table id="mytable" class="table table-bordred table-striped">
                <thead>
                <th>Item Name</th>
                <th>Item Seller</th>
                <th>Item Description</th>
                <th>Highest Bid</th>
                <th>Auction Time Remaining</th>
                </thead>
                <tbody>""")
        sql11 = "SELECT ID_AUCTION, ID_SELLER, FNAME, LNAME, TITLE,DESCRIPTION, EXPIRATION_TIME FROM auction a INNER JOIN item i ON a.ID_ITEM = i.ID_ITEM INNER JOIN user u ON a.ID_SELLER = u.ID_USER ORDER BY EXPIRATION_TIME DESC"
        cursor.execute(sql11)
        result=cursor.fetchall()
        for row in result:
            currentauctionID = row[0]
            selecteduser =row[1]
            fname=row[2]
            lname=row[3]
            title=row[4]
            description=row[5]
            b=row[6]
            import datetime
            import time
            localtime = time.localtime(time.time())
            startdate=str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)
            starttime=str(localtime.tm_hour)+":"+str(localtime.tm_min)+":"+str(localtime.tm_sec)
            a=str(startdate)+" "+str(starttime)
            
            start= datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
            ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
            diff = ends-start
            
            hours = int(diff.seconds // (60 * 60))
            mins = int((diff.seconds // 60) % 60)
            
                    

            print("DIFFERENCE:",diff)
            print("Hours:%s, Minutes:%s"%(hours,mins))
            strdiff=str(diff).split()
            ddiff=strdiff[0]
        
            if(int(ddiff) > 0):
                
            
            #immediately convert to days
                temp=int(ddiff)/86400
                
            #days
                days=temp
                temp=24*(temp-days)
            #hours
                hours=temp
                temp=60 * (temp-hours)
            #minutes
                minutes=temp
                temp=60 * (temp-minutes)
            #seconds
                seconds=temp
              
                if(days>0):
                    timeremaining = "%s days %s hours"%(days,hours)
                elif(hours>0):
                    timeremaining = "%s hours %s minutes"%(hours,minutes)
                elif (minutes>0):
                    timeremaining = "%s minutes %s seconds"%(minutes,seconds)
                elif(seconds>0):
                    timeremaining = "%s seconds"%(seconds)
            else:
                timeremaining = "Auction Complete"
            
                sql12 = "SELECT MAX(PRICE) FROM bid WHERE ID_AUCTION = '%s'"%(currentauctionID)
                if(cursor.execute(sql12)>0):
                    result=cursor.fetchall()
                    for row in result:
                        maxbid=row[0]
                        if(maxbid==""):
                            maxbid="No Bids"
            print("<tr>")
            print("<td>%s</td>"%(title))
            print("<td>%s %s</td>"%(fname,lname))
            print("<td>%s</td>"%(description))
            print("<td>%s</td>"%(maxbid))
            print("<td>%s</td>"%(timeremaining))
            print("</tr>")
            print("""</tbody>
        </table>
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
