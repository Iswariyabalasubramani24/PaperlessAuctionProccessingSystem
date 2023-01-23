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
        print("""<!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Item Search</title>
            <link href="css/bootstrap.min.css" rel="stylesheet">
            <script src="js/jquery.js"></script>
            <script src="js/bootstrap.bundle.js"></script>
        </head>

        <!--Buyers can search the system for particular kinds of item being auctioned and can browse and
        visually re-arrange listings of items within categories.
        This is the buyers search items page -> leads to the auction of a particular item.
        There will be a link to the item's auction is chosen from a list (Bid for items page-->
        <body>
        <!-- Navigation Bar search function -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="b-home.py"><img width="100" src="efast.png"></a>
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






        <div class="container">""")

##            <?php
##
##            if (isset($_POST["submit"])) {
##                $itemToSearch = $_POST['search'];
##
##                if ($itemToSearch == null ) {
##
##                    ?>
##
##                    <div class="container-fluid">
##                        <div class="jumbotron">
##                            <h1 align="center">Search returned no result</h1>
##                        </div>
##                    </div>
##
##                    <?php
##                        exit();
##                }
##
##            $itemToSearch = "%" . $itemToSearch . "%";
##            //$Query = "SELECT * FROM item WHERE TITLE LIKE '%" . $itemToSearch . "%' AND ID_ITEM IN (SELECT ID_ITEM FROM auction WHERE EXPIRATION_TIME > NOW() )";
##            $Query = 'SELECT COUNT(*) AS CON FROM item WHERE TITLE LIKE ? AND ID_ITEM IN (SELECT ID_ITEM FROM auction WHERE EXPIRATION_TIME > NOW() )';
##            $stmt = $pdo->prepare($Query);
##            $stmt->bindParam(1, $itemToSearch, PDO::PARAM_STR);
##            $stmt->execute();
##            $row = $stmt->fetch(PDO::FETCH_ASSOC);
##            if ($row['CON'] > 0) {
##                echo "<br>
##                                <div class=\"container-fluid\">
##                                     <h1 align=\"center\">Here are the results</h1>
##                                       </div>
##                                       <br>";
##
##
##                $Query1 = 'SELECT * FROM item WHERE TITLE LIKE ? AND ID_ITEM IN (SELECT ID_ITEM FROM auction WHERE EXPIRATION_TIME > NOW() )';
##                $stmt1 = $pdo->prepare($Query1);
##                $stmt1->bindParam(1, $itemToSearch, PDO::PARAM_STR);
##                $stmt1->execute();
##
##                while ($row = $stmt1->fetch(PDO::FETCH_ASSOC)) {
##
##                    $image = $row['PIC'];
##                    $itemID = $row['ID_ITEM'];
##                    $title = $row['TITLE'];
##                    $description = $row['DESCRIPTION'];
##                    $catagoryID = $row['ID_CATEGORY'];
##                    $state = $row['ID_STATE'];
##
##                    //$Query2 = "SELECT * FROM auction WHERE ID_ITEM = '$itemID' ";
##                    $Query2 = 'SELECT * FROM auction WHERE ID_ITEM = ? ';
##                    $stmt2 = $pdo->prepare($Query2);
##                    $stmt2->bindParam(1, $itemID, PDO::PARAM_STR);
##                    $stmt2->execute();
##
##                    while ($row = $stmt2->fetch(PDO::FETCH_ASSOC)) {
##                        $exptime = $row['EXPIRATION_TIME'];
##                        $idauction = $row['ID_AUCTION'];
##                        $startprice = $row['START_PRICE'];
##                        $selecteduserID = $row['ID_SELLER'];
##
##
##                        $Query3 = 'SELECT * FROM user WHERE ID_USER = ? ';
##                        $stmt3 = $pdo->prepare($Query3);
##                        $stmt3->bindParam(1, $selecteduserID, PDO::PARAM_STR);
##                        $stmt3->execute();
##                        while ($row = $stmt3->fetch(PDO::FETCH_ASSOC)) {
##                            $seller_first = $row['FNAME'];
##                            $seller_last = $row['LNAME'];
##
##                            //$Query3 = "SELECT MAX(PRICE) AS max_price FROM bid WHERE ID_AUCTION = '$idauction' ";
##                            $Query4 = 'SELECT MAX(PRICE) AS max_price FROM bid WHERE ID_AUCTION = ? ';
##                            $stmt4 = $pdo->prepare($Query4);
##                            $stmt4->bindParam(1, $idauction, PDO::PARAM_STR);
##                            $stmt4->execute();
##
##
##                            while ($row = $stmt4->fetch(PDO::FETCH_ASSOC)) {
##
##                                $currentBid = $row['max_price'];
##
##                                ?>
##
##                                <div class="row">
##
##                                    <div class="col-md-12">
##
##                                        <div class="card">
##                                            <div class="col-12">
##
##                                                    <div class="card-body">
##                                                        <div class="row">
##
##
##                                                            <div class="col-4">
##                                                                <div class="card" >
##                                                                    <img src="<?php echo $image ?>" alt="..."
##                                                                         style="height: 200px">
##                                                                </div>
##                                                            </div>
##
##                                                            <div class="col-8">
##                                                                <h3><?php echo $title; ?></h3>
##
##                                                                <p class="card-title" >
##                                                                    <?php echo $description; ?> </p>
##
##                                                                <a <?php echo "href='profile-other.py?uID=".$selecteduserID."''"?>><?php echo $seller_first." ".$seller_last; ?> </p></a>
##
##                                                                <ul class="list-group list-group-flush">
##                                                                    <li class="list-group-item">
##                                                                        <?php if ($state == 'STATE_01') {
##                                                                            echo "New with sealed box";
##                                                                        } elseif ($state == 'STATE_02') {
##                                                                            echo "New with opened box";
##                                                                        } elseif ($state == 'STATE_03') {
##                                                                            echo "New with defects";
##                                                                        } else {
##                                                                            echo "Used";
##                                                                        } ?>
##                                                                    </li>
##                                                                    <li class="list-group-item">
##                                                                        <?php if (isset($currentBid)) {
##                                                                            echo 'Highest bid is £';
##                                                                            echo $currentBid;
##                                                                        } else {
##                                                                            echo "No bid made yet";
##                                                                        }
##                                                                        ?>
##                                                                    </li>
##                                                                </ul>
##
##
##                                                                <?php
##                                                                $_SESSION['auctionID'] = $idauction;
##                                                                ?>
##
##
##                                                                <div class="card-body">
##                                                                    <div class="row">
##
##                                                                        <form action="searchtobid.py" method="post">
##
##                                                                        <div class="col-6">
##                                                                            <button
##                                                                                    class="btn btn-primary"  type='submit' name='submit' value="<?php echo $_SESSION['auctionID'];  ?>" id="submit" > Go to bidpage
##                                                                            </button>
##
##                                                                        </div>
##
##                                                                        </form>
##
##                                                                        <div class="col-6">
##
##                                                                            <button
##                                                                                    class="btn btn-primary" type='watchlistbtn' onclick="addToWatchlist()" name='watchlistbtn' 
##                                                                                    value="<?php echo $_SESSION['auctionID'];  ?>" id="watchlistbtn" > Add to Watchlist
##                                                                            </button>
##
##                                                                        </div>
##
##
##                                                                    </div>
##                                                                </div>
##
##
##                                                            </div>
##
##                                                        </div>
##                                                    </div>
##
##
##
##                                            </div>
##
##                                            <div class="card-footer">
##                                                <p align="center" class="text-muted">
##                                                    <?php
##                                                    $now = date('Y-m-d H:i:s');
##                                                    $diff=strtotime($exptime)-strtotime($now);
##                                                    if($diff>0) {
##
##                                                        // immediately convert to days
##                                                        $temp = $diff / 86400; // 86400 secs in a day
##
##                                                        // days
##                                                        $days = floor($temp);
##                                                        $temp = 24 * ($temp - $days);
##                                                        // hours
##                                                        $hours = floor($temp);
##                                                        $temp = 60 * ($temp - $hours);
##                                                        // minutes
##                                                        $minutes = floor($temp);
##                                                        $temp = 60 * ($temp - $minutes);
##                                                        // seconds
##                                                        $seconds = floor($temp);
##
##                                                        if ($days > 0) {
##                                                            $timeremaining = "{$days} days {$hours} hours";
##                                                        } elseif ($hours > 0) {
##                                                            $timeremaining = "{$hours} hours {$minutes} minutes";
##                                                        } elseif ($minutes > 0) {
##                                                            $timeremaining = "{$minutes} minutes {$seconds} seconds";
##                                                        } elseif ($seconds > 0) {
##                                                            $timeremaining = "{$seconds} seconds";
##                                                        }
##                                                    }
##                                                    else {$timeremaining = "Auction Complete";}
##                                                    ?>
##                                                    Time remaining: <?php echo $timeremaining; ?>
##                                                </p>
##                                            </div>
##                                        </div>
##
##
##                                    </div>
##                                </div>
##
##                                <br>
##
##                                <?php
##
##                            }}}}
##
##
##
##                } else {
##                    echo "<div class=\"container-fluid\">
##                                  <div class=\"jumbotron\">
##                                     <h1 align=\"center\">Search returned no result</h1>
##                                       </div>
##                                       </div>";
##                }
##
##                //$ExecQuery = MySQLi_query($conn, $Query);
##
##
##
##
##                                } //main submit
##
##
##                                ?>
##        </div>


        print("""<script type="text/javascript">
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






        </body>



        <style>
            .jumbotron {
                background-color: transparent;
            }

            div.scrollmenu {
                background-color: transparent;
                overflow: auto;
                white-space: nowrap;
            }

            div.scrollmenu a {
                display: inline-block;
                color: #777777;
                text-align: center;
                padding: 14px;
                text-decoration: none;
            }

            div.scrollmenu a:hover {
                color: #525252;
            }
        </style>
        </html>""")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
