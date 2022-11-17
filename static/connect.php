<!DOCTYPE html>
<html>
 
<head>
    <title>Insert Page page</title>
</head>
 
<body>
    <center>
        <?php
        $servername = "localhost";
        $username = "username";
        $password = "password";
        $dbname = "wikiPracticas";
        // Create connection
        $conn = new mysqli($servername,
            $username, $password, $dbname);
        
        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: "
                . $conn->connect_error);
        }
        
        $username = $_POST['username'];
        $password = $_POST['password'];
        $email=$_POST['email'];
        $dateofbirth = $_POST['dateofBirth'];

        $sqlquery = "INSERT INTO wikiPracticas.users('$username','$email','$password','$dateofBirth')";
        
        if(mysqli_query($conn, $sqlquery)){
            echo "<h3>data stored in a database successfully."
                . " Please browse your localhost php my admin"
                . " to view the updated data</h3>";
 
            echo nl2br("\n$username\n $email\n "
                . "$password\n $dateofBirth");
        } else{
            echo "ERROR: Hush! Sorry $sqlquery. "
                . mysqli_error($conn);
        }
         
        // Close connection
        mysqli_close($conn);
        ?>
    </center>
</body>
 
</html>