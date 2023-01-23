#!C:/Users/iswar/AppData/Local/Programs/Python/Python37/python.exe
print("Content-Type:text/html\n\r")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Register</title>
<link href="css/bootstrap.min.css" rel="stylesheet">

</head>

<!--Users have roles of seller, buyer or administrator with different privileges.-->

<body>



<form action="insertregister.py" method="post">
<div class="container">

<div align="center">
<img align="center" height="50" src="efast.png">
</div>


<h2>Sign Up</h2>
<p>Please fill in this form to create an account.</p>
<hr>

<label><b>First name</b></label>
<input type="text" placeholder="Enter your first name " name="firstname" id="firstname"  required>

<label><b>Last name</b></label>
<input type="text" placeholder="Enter your last name " name="lastname" id="lastname" required>


<label><b>Email</b></label>
<input type="text" placeholder="Enter your email. This will act as your username " name="email" id="email" required>

<label><b>Password</b></label>
<input type="password" placeholder="Enter your password" name="password" id="password" required>

<label><b>Repeat Password</b></label>
<input type="password" placeholder="Repeat password" name="password-repeat" id="password-repeat" required>

<input type="radio" name="radio" value="ROLE_01"> Buyer<br>
<input type="radio" name="radio" value="ROLE_02"> Seller<br>
<!--         <input type="radio" name="radio" value="ROLE_03"> Administrator<br>
-->

<br>
<br>


<div>

<!--             <button type="submit" class="signupbtn">Sign Up</button>
-->            <input class='btn btn-info btn-lg btn-block btn-sm'
type='submit' name='submit' value='Register' id="submit" />

<button type="button" class="btn btn-warning btn-lg btn-block btn-sm" onclick="window.location='login.php';" >Cancel</button>

</div>


</div>
</form>



<style>


/* Full-width inputs */
input[type=text], input[type=password] {
width: 100%;
padding: 12px 20px;
margin: 8px 0;
display: inline-block;
border: 1px solid #ccc;
box-sizing: border-box;
}

/* Set a style for all buttons */
button {
background-color: #2cbdc6;
color: white;
padding: 14px 20px;
margin: 8px 0;
border: none;
cursor: pointer;
width: 100%;
}

/* Add a hover effect for buttons */
button:hover {
background-color: #2badb6;
}


/* Add padding to containers */
.container {
padding: 150px;
}

/* The "Forgot password" text */
span.psw {
float: right;
padding-top: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
span.psw {
display: block;
float: none;
}
.cancelbtn {
width: 100%;
}
}


/* Extra styles for the cancel button */
.cancelbtn {
padding: 14px 20px;
background-color: #f44336;
}

/* Float cancel and signup buttons and add an equal width */
.cancelbtn, .signupbtn {
float: left;
width: 50%;
}

</style>
""")
            

print("""</body></html>""")
