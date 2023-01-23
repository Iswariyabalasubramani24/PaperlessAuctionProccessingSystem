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
        <title>Create an Auction</title>
        <link href="css/bootstrap.min.css" rel="stylesheet">
        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        -->
        </head>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="s-home.py"><img width="100" src="efast.png"></a>
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
        <body style="background-color: #F0EEEC">
        """)
        
        print("""
        <!--name tag is the most important to transmit to php section-->
        <!--Title-->
        <div class="spacer" style="height: 20px"></div>
        <form action="insertcreateAuction.py" role="form" method="post" enctype="multipart/form-data">
        <div style="width: 70%; margin: 0 auto; float: none; margin-bottom: 20px; ">
        <div class="card">
        <div class="card-header">
        Specify details of your product
        </div>
        <div class="card-body">
        <h5 class="card-title">Title of your product</h5>
        <div class="form-group">
        <label>Use words people would search for when looking for your item</label>
        <input class="form-control" aria-describedby="titleHolder" placeholder="Enter title"
        name="item-title" id="title" required>
        <small class="form-text text-muted">Be descriptive not creative!</small>
        </div>
        </div>
        </div>
        <!-- Item image -->
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Photo</h5>
        <p class="card-text">Upload a photo of your item and improve user confidence by adding an associating
        picture</p>
        <input   type="file" name="upload" required>
        </div>
        </div>
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Item specific</h5>
        <p class="card-text">Select specific details about your item to help buyers find it quickly</p>
        <!-- Item state-->
        <div class="input-group mb-3">
        <div class="input-group-prepend">
        <label class="input-group-text" for="inputGroupSelect01">Item condition &nbsp;</label>
        </div>
        <select class="custom-select" name="item-state" id="inputGroupSelect01">
        <option selected="selected">Select State</option>
        """)
        query="select * from state"
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            stateid=row[0]
            state=row[1]
            print("<option value='%s'>%s</option>"%(stateid,state))
        
       
        print("""
        </select>
        </div>
        <!--Category-->
        <div class="input-group mb-3">
        <div class="input-group-prepend">
        <label class="input-group-text" for="inputGroupSelect01">Category &nbsp; &nbsp; &nbsp; &nbsp;
        &nbsp;
        &nbsp;</label>
        </div>
        <!--<select class="custom-select" id="inputGroupSelect01">-->
        <select id="item-category" name="item-category" class="form-control" required>
        <option selected="selected">Select Category</option>""")
        query="select * from category"
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            categoryid=row[1]
            category=row[2]
            print("<option value='%s'>%s</option>"%(categoryid,category))
        print("""</select>
        </div>
        </div>
        </div>
        <!-- Description -->
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Description</h5>
        <p class="card-text">Add any further details about your item including unique features or
        defects/flaws</p>
        <div class="input-group">
        <div class="input-group-prepend">
        <span class="input-group-text">Item description</span>
        </div>
        <textarea class="form-control" aria-label="With textarea" id="item-description"
        name="item-description" required></textarea>
        </div>
        </div>
        </div>
        <!-- Auction details -->
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Auction details</h5>
        <!-- Start Price -->
        <div class="row">
        <div class="col-sm-6">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Start Price</h5>
        <p class="card-text">Please provide the starting price of your item</p>
        <div class="input-group-prepend">
        <div class="input-group mb-3">
        <div class="input-group-prepend">
        <span class="input-group-text">£</span>
        </div>
        <input type="text" class="form-control" name="item-price"
        aria-label="Amount (to the nearest dollar)" required>
        </div>
        </div>
        </div>
        </div>
        </div>
        <!-- Duration -->
        <div class="col-sm-6">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Reserve Price</h5>
        <p class="card-text">Please provide a reserve price for your auction</p>
        <div class="input-group-prepend">
        <div class="input-group mb-3">
        <div class="input-group-prepend">
        <span class="input-group-text">£</span>
        </div>
        <input type="text" class="form-control" name="item-reserve"
        aria-label="Amount (to the nearest pound)" required>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>
        <div class="spacer" style="height: 30px"></div>
        <div class="row">
        <div class="col">
        <div class="card">
        <div class="card-body">
        <h5 class="card-title">Duration</h5>
        <p class="card-text">Please set the duration of your auction</p>
        <div class="input-group mb-3">
        <div class="input-group-prepend">
        <label class="input-group-text" for="inputGroupSelect02">Duration (min) &nbsp;
        &nbsp; &nbsp; &nbsp; &nbsp;
        &nbsp;</label>
        </div>
        <!--<select class="custom-select" id="inputGroupSelect01">-->
        <select id="item-duration" name="item-duration" class="form-control">
        <option selected="selected">Select Duration</option>""")
       
        query="select * from duration"
        cursor.execute(query)
        result=cursor.fetchall()
        for row in result:
            durationid=row[1]
            duration=row[2]
            print("<option value='%s'>%s</option>"%(durationid,duration))
        print("""
        </select>
        </div>
        </div>
        </div>
        </div>
        </div>
        </div>

        </div>
        </div>
        <!--         <input type='submit' name='submit'>
        -->    
        <div class="container">
        <input class="btn btn-primary btn-danger btn-lg btn-block" type='submit' name='submit' value="List item as new auction">
        <br>

        <br>
        <br>
        </div>
        </form>



        </body>
        </html>

        <!-- 
        <div class="spacer" style="height: 20px"></div>
        <button type="button" class="btn btn-primary btn-danger btn-lg btn-block">List item as new auction</button>
        <button type="button" class="cancelbtn" onclick="window.location='createAuction.py';">List item as new auction</button> -->
        <!--             <button type="submit" class="signupbtn">Sign Up</button>


        <div class="spacer" style="height: 50px"></div>
        </body>

        </html>""")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
