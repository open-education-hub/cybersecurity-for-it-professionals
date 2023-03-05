<?php
   ob_start();
   session_start();
   $hostname="localhost";
   $username="root";
   $password="somenastyrootpass";
   $db="products";

   $dbhandle=mysqli_connect($hostname, $username, $password, $db);

   if (mysqli_connect_errno()) {
	   $msg = "Database connection failed: ";
	   $msg .= mysqli_connect_error();
	   $msg .= " : " . mysqli_connect_errno();
	   exit($msg);
   }
?>

<html>
 <head>
  <title>SIS Online Shop</title>
 </head>
 <body>

 <h1>Welcome to the SIS Online Store</h1>

<?php if(isset($_SESSION["username"])) echo "<p>Welcome ". $_SESSION["username"]. "<a href='logout.php'>Logout</a></p>";
else echo "<p>You are no stranger to us. Please login <a href=\"login.php\">here</a></p>";
?>


    <?php if(isset($_GET['id'])) {
        $query = "select * from products where id=".$_GET['id'];
	$result = mysqli_query($dbhandle, $query ); 
	$row = mysqli_fetch_array($result);
        if (!$row) echo "<p> Unable to find product with ID ". $_GET['id'] ."</p>";
        else
            {
        ?>
        <table>
        <th>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
        </th>
        <tr>
            <td> <?php echo $row{'name'}; ?></td>
            <td> <?php echo $row{'PRICE'}."$"; ?></td>
            <td> <?php echo $row{'description'} ?></td>
         <?php }
   } 
    else {
        ?>
    
    <h2> Here are our products: </h2>
    <?php 
    $query = "select id, name from products";
    $result = mysqli_query($dbhandle, $query ); 
    while ($row = mysqli_fetch_array($result)) {
        echo "<a href=\"" .$_SERVER['PHP_SELF'] ."?id=" .$row['id']. "\">" . $row['name'] . "</a><br/>";

    }
    }
    ?>
</body>
</html>
