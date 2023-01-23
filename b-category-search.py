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
        </body>
        </html>""")
    else:
        print("<script>alert('No User');location.href='index.py';</script>")
else:
    print("Error in DB Connection")
