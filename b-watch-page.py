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
        
        print("""

            <!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Watch List</title>
            <link href="css/bootstrap.min.css" rel="stylesheet">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
            <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
            <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    
            </head>
            <!-- Buyers can watch auctions on items and receive emailed updates on bids
            on those items including notifications when they are outbid.-->
            <body>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="b-home.py">
            <img width="100" src="efast.png">
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent"
                    aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
            </button>
            <div class="col-md-auto">
            </div>
            <div class="collapse navbar-collapse">
            <ul class="nav navbar-nav navbar-right">
            <li><a href="b-myprofile.py"><img height="30px" src="img/user1.png">%s </a></li>"""%(userid))
        print("""</ul>
            </div>
            <button style="margin-left: 10px" type="button" onclick="window.location='buyerlogout.py';" class="btn btn-outline-danger btn-sm ">Logout</button>
            </nav>
            <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <h2>Your Watched Auctions</h2>
                    <div class="table-responsive">
                    <table id="mytable" class="table table-bordred table-striped">
                    <thead>
                    <th>Item Image</th>
                    <th>Item Name</th>
                    <th>Item Description</th>
                    <th>Current Highest Bid</th>
                    <th>Auction End Date</th>
                    <th>Seller</th>
                    <th>Remove</th>
                    </thead>
                    <tbody>
            """)
        sql="SELECT DISTINCT PIC, TITLE, DESCRIPTION, w.ID_AUCTION, EXPIRATION_TIME, FNAME, LNAME, w.ID FROM item i INNER JOIN auction a ON i.ID_ITEM = a.ID_ITEM INNER JOIN user u ON u.ID_USER = a.ID_SELLER INNER JOIN watchlist w ON w.ID_AUCTION = a.ID_AUCTION WHERE w.ID_USER = '%s' ORDER BY EXPIRATION_TIME ASC"%(userid)
        
        if(cursor.execute(sql)==0):
            ##// if there are no watched auctions:
            title = ""
            descr = ""
            fname = ""
            lname = ""
            expiration_datetime= ""
            timeremaining=""
            highestbid = ""
            ID = ""
            pic =""
                ##    //otherwise:
        else:
            result=cursor.fetchall()
            for row in result:
                pic = row[0]
                title = row[1]
                descr = row[2]
                currentauctionID = row[3]
                expiration_datetime = row[4]
                fname = row[5]
                lname = row[6]
                ID = row[7]
                sql2 = "SELECT PRICE FROM bid WHERE ID_AUCTION = '%s' ORDER BY PRICE DESC LIMIT 1"%(currentauctionID)
               
                if(cursor.execute(sql2)==0):
                    #if there are no bids:
                    highestbid = "No bids"
                else:
                    result2=cursor.fetchall()
                    for row1 in result2:
                        highestbid =row1[0]
                        import time
                        localtime = time.localtime(time.time())
                        startdate=str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)
                        starttime=str(localtime.tm_hour)+":"+str(localtime.tm_min)+":"+str(localtime.tm_sec)
                        currenttime=str(startdate)+" "+str(starttime)
                        
                        import datetime
                        a=currenttime
                        b=expiration_datetime
                        print(a,b)
                        start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
                        ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
                        diff = start-ends
                        hours = int(diff.seconds // (60 * 60))
                        mins = int((diff.seconds // 60) % 60)
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
        print("<tr>")
        print("<td><img src='uploads/%s' class='img-rounded' height='70' width='100'></td>"%(pic))
        print("<td>%s</td>"%(title))
        print("<td>%s</td>"%(descr))
        print("<td>%s</td>"%(highestbid))
        print("<td>%s</td>"%(timeremaining))
        print("<td>%s %s </td>"%(fname,lname))
        print("<td> <a class='btn' href='deletewatched.py?ID=%s'><button class='btn btn-danger btn-xs'><span class='glyphicon glyphicon-trash'></span></button></td>"%(ID))
        print("</tr>")
        print("""  </tbody>
        </table>
        </div>
        </div>
        </div>
        </html>
        """)
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
