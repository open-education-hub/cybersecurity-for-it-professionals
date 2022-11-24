<html>
  <head>
    <title>index.php</title>
  </head>
  <body>
    <!--
    <h1>Want Sum File?</h1>
    <form method="get" action="index.php">
      File: <input type="text" name="file"> <br/>
      <input type="submit">
    </form>
    --!>

    <textarea style="height:auto;width:100%" rows="20"> <?php include($_GET['file']) ?></textarea>
  </body>
</html>
