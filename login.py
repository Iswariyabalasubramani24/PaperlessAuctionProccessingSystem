#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-Type:text/html\n\r")
print("""
<!DOCTYPE html>
<html lang="en">
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<title>Login</title>
<link href="css/bootstrap.min.css" rel="stylesheet">

<!-- Custom CSS -->


<!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
<!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
<!--[if lt IE 9]>
<script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
<script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>

-->


</head>



<body>

<div class="container" style="padding: 5%">

<!--form to contain the login functionalitiy-->

<form action="loginvalidation.py" method="post">


<div align="center">
<img src="eFast.png" width="auto" height="80" alt="">
<H1>PAPERLESS AUCTION PROCESSING SYSTEM</H1>
</div>

<br>
<br>

<h2 class="form-signin-heading">Welcome Back!</h2>
<div id="spacer" style="height: 20px"></div>
<div class="input-group mb-3">
<div class="input-group-prepend">
<span class="input-group-text" id="basic-addon1">@</span>
</div>
<input type="text" class="form-control" name="email" id="email" placeholder="Enter email" aria-label="Username" aria-describedby="basic-addon1" class="form" required >
</div>
<div>
<div>
<input type="password" class="form-control" id="password" name="password" placeholder="Password" required >
</div>
<div id="spacer" style="height: 20px"></div>
<!-- <button type="submit" class="btn btn-primary btn-lg btn-block btn-sm">Login</button> -->
<input class="btn btn-primary btn-lg btn-block btn-sm" type='submit' name='submit' value='Login' id="submit" />
</div>
<div id="spacer2" style="height: 20px"></div>
<div>
<button type="button" class="btn btn-success btn-lg btn-block btn-sm" onclick="window.location='./register.py';">Sign up here</button>
</div></form>
        </div>
        <style>
        </style>

        </body>

        </html>


<style>
    .jumbotron {
        background-color: transparent;
    }

</style>""")




















