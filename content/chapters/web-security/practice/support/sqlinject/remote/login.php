<html>
  <head>
    <title>login.php</title>
  </head>
  <body>

<?php
  $hostname="localhost";
  $username="root";
  $password="somenastyrootpass";
  $db="users";

  $dbhandle=mysqli_connect($hostname, $username, $password, $db);

  if (mysqli_connect_errno()) {
	  $msg = "Database connection failed: ";
	  $msg .= mysqli_connect_error();
	  $msg .= " : " . mysqli_connect_errno();
	  exit($msg);
  }

  $query = "SELECT * from users WHERE name='" . $_POST["username"] ."' AND password='" . $_POST["password"] ."'";
  /* echo "<p>Query: " . $query . "</p>"; */

  $result = mysqli_query($dbhandle, $query ); 
  $row = mysqli_fetch_array($result);
  if ( !$row )
    echo "<p>User/password combination not found!</p>";
  else {
    echo "<p>User: " . $row{'name'}. "</p>";
    echo "<p>Secret: " . $row{'secret'} . "</p>";
  }
?>

  </body>
</html>
