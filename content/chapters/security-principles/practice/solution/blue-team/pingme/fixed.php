<html>
  <head>
    <title>fixed.php</title>
  </head>
  <body>
    <h1>SUPER UBER MEGA PING SERVER</h1>
    <form method="post" action="fixed.php">
      Target: <input type="text" name="target"> <br/>
      <input type="submit">
    </form>

    <p>Some characters will be stripped! Can you still do it?</p>
    <?php
     $string=str_replace(";", " ", $_POST["target"]);
     $string=str_replace("&", " ", $string);
     $string=preg_match('/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\z/', $string);
    ?>
    <p>Target: <?php echo $string; ?>
    <p>Result: </p>
    <textarea style="height:auto;width:100%" rows="20"> <?php system("ping -c 3 " . $string) ?></textarea>

  </body>
</html>

