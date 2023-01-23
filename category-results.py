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
        
        changeByCategory=form.getvalue('changeByCategory')
        changeState=form.getvalue('changeOfState')
        expSort=form.getvalue('sortExpTime')
        #print(changeByCategory,changeState,expSort)
        print("""<html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Homepage</title>
            <link href="css/bootstrap.min.css" rel="stylesheet">
            <script src="js/jquery.js"></script>
            <script src="js/bootstrap.bundle.js"></script>
            </head>
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
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <form action="b-item-search.py" method="post" class="form-inline my-2 my-lg-0">
            <div>
            <select id="item-category" name="item-category" class="form-control" required>
            <option selected="selected">Select Item</option>""")
        query="select * from item"
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            itemid=row[1]
            title=row[3]
            print("<option value='%s'>%s</option>"%(title,title))
        print("""
            </select>
            
            </div>
            <ul class="navbar-nav mr-auto">
            <li class="nav-item" style="padding-left: 10px; padding-right: 10px ">
            <input type="submit" class="btn btn-primary navbar-btn" value="Search by Item"/>
            </a>
            </li>
            </ul>
            
            </form>
            </div>
            </div>
            <div class="collapse navbar-collapse">
            <ul class="navbar-nav ml-auto">
            <li><a href="b-myprofile.py"><img height="30px" src="img/user1.png"> <?php echo "Hi "; echo  $_SESSION['first_name'] ; echo " "; echo   $_SESSION['last_name'] ;   ?> </a></li>
            </ul>
            </div>
            <button style="margin-left: 10px" type="button" onclick="window.location='buyerlogout.py';" class="btn btn-outline-danger btn-sm ">Logout</button>
            </nav>
            <style type="text/css">
                /* Formatting search box */
                .search-box{
                    width: 300px;
                    position: relative;
                    display: inline-block;
                    font-size: 14px;
                }
                .search-box input[type="text"]{
                    height: 32px;
                    padding: 5px 10px;
                    border: 1px solid #CCCCCC;
                    font-size: 14px;
                }
                .result{
                    background-color: white;
                    position: absolute;
                    z-index: 999;
                    top: 100%;
                    left: 0;
                }
                .search-box input[type="text"], .result{
                    width: 100%;
                    box-sizing: border-box;
                }
                /* Formatting result items */
                .result p{
                    margin: 0;
                    padding: 7px 10px;
                    border: 1px solid #20b5dd;
                    border-top: none;
                    cursor: pointer;
                }
                .result p:hover{
                    background: #f2f2f2;
                }
            </style>

            <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
            <script type="text/javascript">
                $(document).ready(function(){
                    $('.search-box input[type="text"]').on("keyup input", function(){
                        /* Get input value on change */
                        var inputVal = $(this).val();
                        var resultDropdown = $(this).siblings(".result");
                        if(inputVal.length){
                            $.get("backend-search.py", {term: inputVal}).done(function(data){
                                // Display the returned data in browser
                                resultDropdown.html(data);
                            });
                        } else{
                            resultDropdown.empty();
                        }
                    });

                    // Set search input value on click of result item
                    $(document).on("click", ".result p", function(){
                        $(this).parents(".search-box").find('input[type="text"]').val($(this).text());
                        $(this).parent(".result").empty();
                    });
                });
            </script>


            <script type="text/javascript">
                function addToWatchlist() {

                   var auction_id = document.getElementById("watchlistbtn").value;   

                   var xhttp;
                    xhttp = new XMLHttpRequest();
                    xhttp.onreadystatechange = function() {
                        if (this.readyState == 4 && this.status == 200) {
                            if (this.responseText != ""){
                                alert(this.responseText);
                            } else {
                                alert("Added to watchlist")
                            }
                            
                        }
                    };


                    var parameters = "auctionID="+auction_id;
                    xhttp.open("POST", "add-watchlist.py/?"+parameters, true);
                    xhttp.send();



                }
            </script>
            <script>
            function showUser() {
                            
                    var str = document.getElementById("changeByCategory").value;
                    

                    var xhttp;
                    xhttp = new XMLHttpRequest();

                    //changing of state 
                    var w = document.getElementById("changeOfState");
                    var changeState = w.options[w.selectedIndex].value;

                    //exptime
                    var r = document.getElementById("sortExpTime");
                    var sortExp = r.options[r.selectedIndex].value;

                    var parameters = "q="+str+"&changestate="+changeState+"&sortexp="+sortExp;
                    xhttp.open("GET","category-results.py?"+parameters,true);
                    xhttp.send();

                    xhttp.onreadystatechange = function() {
                        if (this.readyState == 4 && this.status == 200) {
                            document.getElementById("txtHint").innerHTML = this.responseText;
                        }
                    };
            }

            </script>
            
        <style>
        table
        {
        width: 100%;
        border-collapse: collapse;
        }
        table, td, th
        {
        border: 1px solid black;
        padding: 5px;
        }
        th{
        text-align: left;
        }
        </style>
        </head>
        <body>
         <div class="container">
            <br>
            <br>
            <form action='category-results.py' method='POST'>
            <select class="custom-select mb-2 mr-sm-2 mb-sm-0" name="changeByCategory" id="changeByCategory">
            <option value="">Filter via category</option>""")
        query="select * from category"
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            categoryid=row[1]
            category=row[2]
            print("<option value='%s'>%s</option>"%(categoryid,category))
        print("""</select>

            <br> <br>
            <select class="custom-select mb-2 mr-sm-2 mb-sm-0" name="changeOfState" id="changeOfState">
            <option  value=" "> Filter by current state of item </option>
              <option  value="AND ID_STATE = 'STATE_01'"> NEW WITH SEALED BOX </option>
              <option  value="AND ID_STATE = 'STATE_02'"> NEW WITH OPENED BOX </option>
              <option  value="AND ID_STATE = 'STATE_03'"> NEW WITH DEFECTS </option>
              <option  value="AND ID_STATE = 'STATE_04'"> USED </option>
              </select>
            <br>
          <br>

          <select class="custom-select mb-2 mr-sm-2 mb-sm-0" name="sortExpTime" id="sortExpTime">
          <option  value=" "> Filter by expiry of item </option>
          <option  value="ORDER BY EXPIRATION_TIME DESC"> Sort by newest auctions </option>
          <option  value="ORDER BY EXPIRATION_TIME ASC"> Sort by auctions about to expire </option>
          </select>
       
        </div>
        <br>
        <div class="container">
       <input class="btn btn-outline-success my-2 my-sm-0" type='submit' id="submit" name="submit" value="Search">
        </div>
         </form>
        <div class="container">""")
      
        sql="SELECT COUNT(*) AS CON FROM auction WHERE ID_ITEM IN ( SELECT ID_ITEM FROM item WHERE ID_CATEGORY ='%s' %s %s)"%(changeByCategory,changeState,expSort)
        #print(sql)
        cursor.execute(sql)
        result=cursor.fetchone()
        if(result[0]>0):
            print("<br>")
            print("<div class='container-fluid'><h1 align='center'>Here are the results</h1>")
            print("</div><br>")
            sql1="SELECT ID_ITEM FROM auction WHERE  ID_ITEM IN ( SELECT ID_ITEM FROM item WHERE ID_CATEGORY ='%s' %s %s)"%(changeByCategory,changeState,expSort)
            cursor.execute(sql1)
            result1=cursor.fetchall()
            for row in result1:
                itemID=row[0]
        
                sqlint=" SELECT * FROM item WHERE ID_ITEM = '%s' "%(itemID)
                cursor.execute(sqlint)
                result2=cursor.fetchall()
                for row2 in result2:
                    itemID=row2[1]
                    image=row2[2]
                    title=row2[3]
                    description=row2[4]
                    catagoryID=row2[5]
                    state=row2[6]
               
                    Query2 = "SELECT * FROM auction WHERE ID_ITEM = '%s' "%(itemID)
                    cursor.execute(Query2)
                    result3=cursor.fetchall()
                    for row3 in result3:
                        idauction=row3[1]
                        startprice=row3[4]
                        exptime=row3[6]
                        Query3="SELECT MAX(PRICE) AS max_price FROM bid WHERE ID_AUCTION='%s'"%(idauction)
                        cursor.execute(Query3)
                        result4=cursor.fetchall()
                        for row4 in result4:
                            currentBid=row4[0]

        print("""<div class="row">
                <div class="col-md-12"><div class="card">
                <div class="col-12">
                <div class="card-body">
                <div class="row">
                <div class="col-4">
                <div class="card" >
                <img src="uploads/%s" alt="..." style="height: 200px"></div></div>"""%(image))
        print("""<div class="col-8"><h3>%s</h3>"""%(title))
        print("""<p class="card-title" >%s</p>"""%(description))
        print("""<ul class="list-group list-group-flush"><li class="list-group-item">""")
        if(state=='STATE_01'):
              print("New with sealed box")
        elif(state=='STATE_02'):
              print("New with opened box")
        elif(state=='STATE_03'):
              print("New with defects")
        else:
              print("Used")
        print("</li>")
        print("<li class='list-group-item'>")
        if(currentBid):
            print("Highest bid is £ %s"%(currentBid))
        else:
            print("No bid made yet")
        print("</li></ul>")
        auctionID=idauction
        print("<div class='card-body'>")
        print("<div class='row'>")
        print("<form action='searchtobid.py' method='post'>")
        print("<div class='col-6'>")
        print("<button class='btn btn-primary'  type='submit' name='submit' value='%s' id='submit' > Go to bidpage"%(auctionID))
        print("</button>")
        print("</div></form>")
        print("<div class='col-6'>")
        print("<form action='addtowatchlist.py' method='post'>")
        print("<button class='btn btn-primary' type='submit' name='watchlistbtn' value='%s' id='watchlistbtn'> Add to Watchlist"%(auctionID))
        print("</button>")
        print("</form>")
        print("</div></div></div></div></div></div></div>")
        print("<div class='card-footer'><p align='center' class='text-muted'>")
        import time
        localtime = time.localtime(time.time())
        startdate=str(localtime.tm_year)+"-"+str(localtime.tm_mon)+"-"+str(localtime.tm_mday)
        starttime=str(localtime.tm_hour)+":"+str(localtime.tm_min)+":"+str(localtime.tm_sec)
        stime=str(startdate)+" "+str(starttime)
        
        import datetime
        a=stime
        b=exptime
        start = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
        ends = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')
        diff = start-ends
        
        hours = int(diff.seconds // (60 * 60))
        mins = int((diff.seconds // 60) % 60)
        print("DIFFERENCE:",diff)
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
        
        print("Time remaining: %s</p>"%(timeremaining))
        print("</div></div></div></div><br>")
        #print("<div class='container-fluid'><div class='jumbotron'>")
        #print("<h1 align='center'>Search returned no result</h1>")
        #print("</div></div>")
        print("""</div></body></html>""")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
