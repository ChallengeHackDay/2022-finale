<?php

if (isset($_POST['password'])) {
        if (
            "Flipper2015" === $_POST['password']
        ) {
            $loggedUser = true;
        } else {
            $errorMessage = sprintf('Wrong password');
        }
}
?>

<?php if(!isset($loggedUser)): ?>
<form action="index.php" method="post" style="width:30%; margin:auto;">
    <?php if(isset($errorMessage)) : ?>
        <div class="alert alert-danger" role="alert">
            <?php echo $errorMessage; ?>
        </div>
    <?php endif; ?>
    <div class="mb-3" style="text-align:center">
        <label for="password" class="form-label" style="color:white"><b>Password</b></label>
        <input type="password" class="form-control" id="password" name="password">
    
    <button type="submit" class="btn btn-primary" style="margin-top:3%">Send</button>
    </div>
</form>
<?php else: ?>
    <div class="alert alert-success" role="alert">
        Hello Elliot, <br> We have a message for you : HACKDAY{J01N_FS0C13TY}
    </div>
<?php endif; ?>