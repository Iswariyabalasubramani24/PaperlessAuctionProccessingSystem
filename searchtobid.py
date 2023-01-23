#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-type:text/html\r\n\r\n")
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
        auctionid=form.getvalue('submit')

        import time
        localtime = time.localtime(time.time())
        startdate=str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)
        starttime=str(localtime.tm_hour)+":"+str(localtime.tm_min)+":"+str(localtime.tm_sec)
        stime=str(startdate)+" "+str(starttime)
        #insert to traffic table
        insertquery="insert into traffic(id_view,id_auction,id_user) values('%s','%s','%s')"%(stime,auctionid,userid)
        cursor.execute(insertquery)
        db.commit()
        #end
        query2="""SELECT ite.PIC,ite.TITLE,ite.DESCRIPTION,auc.START_PRICE,auc.START_TIMESTAMP,auc.EXPIRATION_TIME,
          cat.CATEGORY,sta.STATE,auc.ID_SELLER,acc.FNAME,acc.LNAME FROM ((((item ite INNER JOIN auction auc ON auc.ID_ITEM = ite.ID_ITEM)
          INNER JOIN category cat ON ite.ID_CATEGORY = cat.ID_CATEGORY) INNER JOIN state sta ON ite.ID_STATE = sta.ID_STATE)
          INNER JOIN user acc ON acc.ID_USER = auc.ID_SELLER)WHERE auc.ID_AUCTION = '%s'"""%(auctionid)
        cursor.execute(query2)
        qresult=cursor.fetchall()
        for rows in qresult:
            itempic=rows[0]
            itemtitle=rows[1]
            itemdescription=rows[2]
            aucstartprice=rows[3]
            aucstarttime=rows[4]
            aucexpiretime=rows[5]
            category=rows[6]
            state=rows[7]
            idseller=rows[8]
            accfname=rows[9]
            acclname=rows[10]
            print("""
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Create an Auction</title>
            <link href="css/bootstrap.min.css" rel="stylesheet">
            <script src="js/jquery.js"></script>
            <script src="https://npmcdn.com/tether@1.2.4/dist/js/tether.min.js"></script>
            <script src="js/bootstrap.min.js"></script>
            </head>
            <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="b-home.py">
            <img width="100" src="efast.png">
            </a>
            <ul class="navbar-nav ml-auto">
            <button style="margin-left: 10px" type="button" onclick="window.location='buyerlogout.py';" class="btn btn-outline-danger btn-sm ">Logout</button>
            </ul>
            </nav>
            <body onload = "load_bid_page()">
            <form action='insertbid.py' name='bidpage' method='post'>
            <div style="padding-right: 3%; padding-left: 3%">
            <br>
            <button type="button" onclick="window.location='category-results.py';" class="btn btn-primary btn-sm">Back to search results</button>
            <div id="spacer" style="height: 20px"></div>
            <div class="card">""")
            #print('<div class="card-header" id="seller_profile">Auctioned by:<a href=profile-other.py?Uid=%s> %s %s</a></div>'%(idseller,accfname,acclname))
            print('<div class="card-header" id="seller_profile">Auctioned by:<a href=#> %s %s %s</a></div>'%(idseller,accfname,acclname))
            print("""<div class="card-body"><div class="row"><div class="col-4"><div class="card" style="height: 100%">""")
            print("""<img id="item_pic" src="uploads/%s" alt="" class="img-thumbnail" style="height: 200px">"""%(itempic))
            print("""</div></div><div class="col-8"><div class="card text-left">""")
            print("""<div id="item_title" class="card-header">%s</div>"""%(itemtitle))
            print("""<div class="card-block" style="padding: 20px">
            <h4 class="card-title" id="highest_bid">Current highest bid: </h4>
            <div id="spacer" style="height: 20px"></div>
            <div class="input-group-prepend">
            <div class="input-group mb-3">
            <div class="input-group-prepend">
            <span class="input-group-text">£</span>
            </div>
            <input type='hidden' name='auctionid' value='%s'>
            <input type="text" name='bidamt' class="form-control" aria-label="Amount (to the nearest dollar)" id="bidamt">
            <span class="input-group-btn">
            <button class="btn btn-primary" type="submit"  >Submit bid!</button>
            </span>
            </div></div></div>
            <div id="remaining_time" class="card-footer text-muted">Remaining Time"""%(auctionid))
            
            import datetime
            a=aucstarttime
            b=aucexpiretime
            start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
            ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
            diff = start-ends
            print(diff)
            hours = int(diff.seconds // (60 * 60))
            mins = int((diff.seconds // 60) % 60)
            print("Hours:%s, Minutes:%s"%(hours,mins))
                               
            print("""</div></div></div></div></div></div><br>
            <ul class="nav nav-tabs" role="tablist">
            <li class="nav-item">
            <a class="nav-link active" data-toggle="tab" href="#home">Description</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" data-toggle="tab" href="#menu1">Product Details</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" data-toggle="tab" href="#bid_history">Bids History</a>
            </li>
            </ul>""")
            print("""<div class="tab-content">
            <div id="home" class="container tab-pane active">
            <br><h3 id="item_title2">%s</h3>
            <p id="item_description">%s</p></div>"""%(itemtitle,itemdescription))
          
            print("""<div id="menu1" class="container tab-pane fade">
            <br><h3>Product Details</h3>
            <p id="item_details">%s <br>%s <br>%s</p></div>"""%(itemdescription,category,state))
            print("""<div id="bid_history" class="container tab-pane fade">
            <br><h3>Bids History</h3>
            <p id="starting_bid">$ Start Price %s on Start Date %s</p>
            <p id="bid_history_log"> </p>
            </div>"""%(aucstartprice,aucstarttime))
            print("""</div><br></form></body></html>""")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
