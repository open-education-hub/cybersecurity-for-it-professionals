<html>
  <head>
    <title>index.php</title>
  </head>
  <body>
    <h1>SUPER UBER MEGA PING SERVER</h1>
    <form method="post" action="index.php">
      Target: <input type="text" name="target"> <br/>
      <input type="submit">
    </form>

    <p>Target: <?php echo $_POST["target"]; ?>
    <p>Result: </p>
    <textarea style="height:auto;width:100%" rows="20"> <?php system("ping -c 3 " . $_POST["target"]) ?></textarea>
  </body>
</html>
