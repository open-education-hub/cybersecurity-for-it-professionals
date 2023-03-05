<?php
   ob_start();
   session_start();
?>

<?
   // error_reporting(E_ALL);
   // ini_set("display_errors", 1);
?>

<html lang = "en">
   
   <head>
      <title>SIS Online Shop</title>
   </head>
    
   <body>
     <?php if(!isset($_SESSION['username'])) { ?>

      <h2>Enter Username</h2> 
      <div class = "container form-signin">
         
         <?php
            $msg = '';
            
            if (isset($_POST['login']) && !empty($_POST['username'])) {
                
                  $_SESSION['valid'] = true;
                  $_SESSION['timeout'] = time();
                  $_SESSION['username'] = $_POST['username'];
                  
                  echo 'You have succesfully logged in. User: '. $_POST['username'];
               }
            
         ?>
      </div> 
      
      <div class = "container">
      
         <form role = "form" action = "login.php" method = "post">
            <h4><?php echo $msg; ?></h4>
            <input type = "text" name = "username" placeholder = "Username" 
               required autofocus></br>
            <button type = "submit" name = "login">Login</button>
         </form>
<?php }
else echo "You are already logged in as user: ".$_SESSION['username']; ?>
            
         Click <a href = "logout.php" title = "Logout">here to clean session.</a>
         
      </div> 
      
   </body>
</html>

