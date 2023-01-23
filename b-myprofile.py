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
    if(userrole=="ROLE_01"):
        query="select fname,lname,email,pass from user where id_user='%s' and id_role='%s'"%(userid,userrole)
        cursor.execute(query)
        result=cursor.fetchone()
        fname=result[0]
        lname=result[1]
        email=result[2]
        pwd=result[3]
        print("""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Seller MyProfile</title>
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/profile.css" rel="stylesheet">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
    <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>

</head>





<body>



<nav class="navbar navbar-light bg-light">
<a class="navbar-brand" href="s-home.py">
<img src="eFast.png" width="100" height="30" alt="">
</a>
 <ul class="navbar-nav ml-auto">
            <button style="margin-left: 10px" type="button" onclick="window.location='buyerlogout.py';" class="btn btn-outline-danger btn-sm ">Logout</button>
            </ul>
</nav>



<h1 class="display-3"> &nbsp My Profile </h1>

<div class="container">
    <div class="row">
        <div class="col-sm-6 col-md-6">
            <div class="panel panel-default panel-info Profile">
                <div class="panel-body">
                    <div class="form-horizontal">
                        <form>
                            <div class="form-group">
                                <label class="col-sm-2 control-label">First Name</label>
                                <div class="col-sm-6">
                                    <input class="form-control" type="text" name="firstName"
                                           placeholder="" ng-model="me.firstName" value='%s'>"""%(fname))
    print("""</div>
                            </div>
                            <div class="form-group">
                                <label class="col-sm-2 control-label">Last Name</label>
                                <div class="col-sm-6">
                                    <input class="form-control" type="text" name="lastName"
                                           placeholder="" ng-model="me.lastName" value='%s'>"""%(lname))
    print("""</div>
                            </div>
                            <div class="form-group">
                                <label class="col-sm-2 control-label">Email</label>
                                <div class="col-sm-6">
                                    <input class="form-control" type="text" name="email"
                                           readonly placeholder="" ng-model="me.email" value='%s'>"""%(email))
    print(""" </div>
</div>
<div class="form-group">
<label class="col-sm-2 control-label">Password</label>
<div class="col-sm-6">
<input class="form-control" type="text" name="password"
placeholder="" ng-model="me.email" value='%s'>"""%(pwd))
    print("""</div>
</div>
<div class="form-group">
<div class="col-sm-offset-2 col-sm-10">
<button class="btn btn-primary" ng-click="updateMe()">Update</button>
</div>
</div>
</form>
</div>
</div>  <!-- end form-horizontal -->
</div> <!-- end panel-body -->

</div> <!-- end panel -->

<div class="col-sm-3">
<div class="rating-block">
<h4>Average user rating</h4>
<h2 class="bold padding-bottom-7">4.3 <small>/ 5</small></h2>
<button type="button" class="btn btn-warning btn-sm" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn-warning btn-sm" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn-warning btn-sm" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn-default btn-grey btn-sm" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn-default btn-grey btn-sm" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
</div>
</div>
<div class="col-sm-3">
<h4>Rating breakdown</h4>
<div class="pull-left">
<div class="pull-left" style="width:35px; line-height:1;">
<div style="height:9px; margin:5px 0;">5 <span class="glyphicon glyphicon-star"></span></div>
</div>
<div class="pull-left" style="width:180px;">
<div class="progress" style="height:9px; margin:8px 0;">
<div class="progress-bar progress-bar-success" role="progressbar" aria-valuenow="5" aria-valuemin="0" aria-valuemax="5" style="width: 1000%">
<span class="sr-only">80% Complete (danger)</span>
</div>
</div>
</div>
<div class="pull-right" style="margin-left:10px;">1</div>
</div>
<div class="pull-left">
<div class="pull-left" style="width:35px; line-height:1;">
<div style="height:9px; margin:5px 0;">4 <span class="glyphicon glyphicon-star"></span></div>
</div>
<div class="pull-left" style="width:180px;">
<div class="progress" style="height:9px; margin:8px 0;">
<div class="progress-bar progress-bar-primary" role="progressbar" aria-valuenow="4" aria-valuemin="0" aria-valuemax="5" style="width: 80%">
<span class="sr-only">80% Complete (danger)</span>
</div>
</div>
</div>
<div class="pull-right" style="margin-left:10px;">1</div>
</div>
<div class="pull-left">
<div class="pull-left" style="width:35px; line-height:1;">
<div style="height:9px; margin:5px 0;">3 <span class="glyphicon glyphicon-star"></span></div>
</div>
<div class="pull-left" style="width:180px;">
<div class="progress" style="height:9px; margin:8px 0;">
<div class="progress-bar progress-bar-info" role="progressbar" aria-valuenow="3" aria-valuemin="0" aria-valuemax="5" style="width: 60%">
<span class="sr-only">80% Complete (danger)</span>
</div>
</div>
</div>
<div class="pull-right" style="margin-left:10px;">0</div>
</div>
<div class="pull-left">
<div class="pull-left" style="width:35px; line-height:1;">
<div style="height:9px; margin:5px 0;">2 <span class="glyphicon glyphicon-star"></span></div>
</div>
<div class="pull-left" style="width:180px;">
<div class="progress" style="height:9px; margin:8px 0;">
<div class="progress-bar progress-bar-warning" role="progressbar" aria-valuenow="2" aria-valuemin="0" aria-valuemax="5" style="width: 40%">
<span class="sr-only">80% Complete (danger)</span>
</div>
</div>
</div>
<div class="pull-right" style="margin-left:10px;">0</div>
</div>
<div class="pull-left">
<div class="pull-left" style="width:35px; line-height:1;">
<div style="height:9px; margin:5px 0;">1 <span class="glyphicon glyphicon-star"></span></div>
</div>
<div class="pull-left" style="width:180px;">
<div class="progress" style="height:9px; margin:8px 0;">
<div class="progress-bar progress-bar-danger" role="progressbar" aria-valuenow="1" aria-valuemin="0" aria-valuemax="5" style="width: 20%">
<span class="sr-only">80% Complete (danger)</span>
</div>
</div>
</div>
<div class="pull-right" style="margin-left:10px;">0</div>
</div>
</div>


</div>
<h2> Review history </h2>
<div class="row">
<div class="col-sm-12">
<hr/>
<div class="review-block">
<div class="row">
<div class="col-sm-3">
<img src="http://dummyimage.com/60x60/666/ffffff&text=No+Image" class="img-rounded">
<div class="review-block-name"><a href="#"></a></div>
<div class="review-block-date"><br/></div>
</div>
<div class="col-sm-9">
<div class="review-block-rate">
<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn-warning btn-xs" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
<button type="button" class="btn btn-default btn-grey btn-xs" aria-label="Left Align">
<span class="glyphicon glyphicon-star" aria-hidden="true"></span>
</button>
</div>
<!--<div class="review-block-title">Excellent blueberry muffins!!</div>
<div class="review-block-description">These were very good muffins. These were very good muffins. These were very good muffins. These were very good muffins. These were very good muffins. These were very good muffins.</div>-->
</div>
</div>
<hr/>



</div>
</div>
</div>
<div class="clearfix"></div>
<ul class="pagination pull-right">
<li class="disabled"><a href="#"><span class="glyphicon glyphicon-chevron-left"></span></a></li>
<li class="active"><a href="#">1</a></li>
<li><a href="#">2</a></li>
<li><a href="#">3</a></li>
<li><a href="#">4</a></li>
<li><a href="#">5</a></li>
<li><a href="#"><span class="glyphicon glyphicon-chevron-right"></span></a></li>
</ul>

</div>

</div> <!-- /container -->

<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script src="http://getbootstrap.com/dist/js/bootstrap.min.js"></script>

<div class="container">
<div class="row">


<div class="col-md-12">
<h2>BID History</h2>
<div class="table-responsive">


<table id="mytable" class="table table-bordred table-striped">

<thead>
<th>Item Name</th>
                        <th>Item Seller</th>
                        <th>Item Description</th>
                        <th>Your Bid</th>
                        <th>Auction Time Remaining</th>
                        <th>Bid Status</th>
                        <th>Feedback</th>
</thead>
<tbody>""")
    sql="SELECT PRICE, ID_AUCTION FROM bid WHERE ID_BUYER = '%s' ORDER BY TIME DESC"%(userid)
   
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        bidamount=row[0]
        currentauctionID=row[1]
        sql1 = "SELECT TITLE, DESCRIPTION, EXPIRATION_TIME, FNAME, LNAME,ID_USER FROM auction a INNER JOIN item i ON a.ID_ITEM = i.ID_ITEM INNER JOIN user u ON u.ID_USER = a.ID_SELLER WHERE ID_AUCTION = '%s'"%(currentauctionID)
       
        cursor.execute(sql1)
        result=cursor.fetchall()
        for row in result:
            title=row[0]
            description=row[1]
            expiration_time=row[2]
            fname=row[3]
            lname=row[4]
            iduser=row[5]
        
         
            import time
            localtime = time.localtime(time.time())
            startdate=str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)
            starttime=str(localtime.tm_hour)+":"+str(localtime.tm_min)+":"+str(localtime.tm_sec)
            stime=str(startdate)+" "+str(starttime)

            import datetime
            a=stime
            b=expiration_time
            start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
            ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
            diff = ends-start
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

        
            sql3="SELECT PRICE, RESERVEd_PRICE FROM bid b INNER JOIN auction a ON a.ID_AUCTION = b.ID_AUCTION WHERE b.ID_AUCTION = '%s' ORDER BY PRICE DESC LIMIT 1"%(currentauctionID)
            
            cursor.execute(sql3)
            results=cursor.fetchall()
            for rows in results:
                highestbid=rows[0]
                reserveprice=rows[1]
                if(highestbid > bidamount):
                    bidstatus = 'Outbid'
                elif(highestbid == bidamount and timeremaining == "Auction Complete" and reserveprice <= bidamount):
                    bidstatus = "You're a winner!"
                elif(highestbid == bidamount and timeremaining != "Auction Complete"):
                    bidstatus = 'Highest Bid'
                elif(highestbid == bidamount and timeremaining == "Auction Complete" and reserveprice > bidamount):
                    bidstatus= 'Reserve not met'
                    
            print("<tr><td>%s</td>"%(title))
            print("<td>%s %s</td>"%(fname,lname))
            print("<td>%s</td>"%(description))
            print("<td>%s</td>"%(bidamount))
            print("<td>%s</td>"%(timeremaining))
            print("<td>%s</td>"%(bidstatus))
            print("<td>")
            if(bidstatus == "You're a winner!"):
                print("<a href='seller-rating.php?aID=%s'> <button class = 'btn button3 btn-xs'>"%(currentauctionID))
                print("<span class ='glyphicon glyphicon-pencil background-color='#A9A9A9'></span></button></a>")
            else:
                print("<a class='button2'><button class = 'btn button2 btn-xs'>")
                print("<span class='glyphicon glyphicon-ok' background-color='#4CAF50'></span></button>")
            print("</centre></td>")
                
                  
            
            
            
            print("</tr>")
        print("""</tbody>

                </table>

                <div class="clearfix"></div>
                <ul class="pagination pull-right">
                    <li class="disabled"><a href="#"><span class="glyphicon glyphicon-chevron-left"></span></a></li>
                    <li class="active"><a href="#">1</a></li>
                    <li><a href="#">2</a></li>
                    <li><a href="#">3</a></li>
                    <li><a href="#">4</a></li>
                    <li><a href="#">5</a></li>
                    <li><a href="#"><span class="glyphicon glyphicon-chevron-right"></span></a></li>
                </ul>

            </div>

        </div>
    </div>
</div>



<div class="modal fade" id="delete" tabindex="-1" role="dialog" aria-labelledby="edit" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal" aria-hidden="true"><span class="glyphicon glyphicon-remove" aria-hidden="true"></span></button>
                <h4 class="modal-title custom_align" id="Heading">Delete this entry</h4>
            </div>
            <div class="modal-body">

                <div class="alert alert-danger"><span class="glyphicon glyphicon-warning-sign"></span> Are you sure you want to delete this bid?</div>

            </div>
            <div class="modal-footer ">""")
        print("""<a href='deleteauction.py?aid=%s'><button type="button" class="btn btn-success" ><span class="glyphicon glyphicon-ok-sign"></span> Yes</button>"""%(currentauction))
        print("""<button type="button" class="btn btn-default" data-dismiss="modal"><span class="glyphicon glyphicon-remove"></span> No</button>
            </div>
        </div>
        <!-- /.modal-content -->
    </div>
    <!-- /.modal-dialog -->
</div>



</body>

</html>""")
