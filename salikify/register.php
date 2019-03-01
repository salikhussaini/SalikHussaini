<?php
function sanitizeFormPassword($inputText) {
	$inputText = strip_tags($inputText);
	return $inputText;
}
function sanitizeFormUsername($inputText) {
	$inputText = strip_tags($inputText);
	$inputText = str_replace(" ", "", $inputText);
	return $inputText;
}
function sanitizeFormString($inputText) {
	$inputText = strip_tags($inputText);
	$inputText = str_replace(" ", "", $inputText);
	$inputText = ucfirst(strtolower($inputText));
	return $inputText;

}


if ( isset($_POST['registerButton'] )) {
	echo 'Register button was pressed';

	$username = sanitizeFormUsername($_POST['username']);

	$firstName = sanitizeFormUsername($_POST['firstName']);

	$LastName = sanitizeFormUsername($_POST['LastName']);

	$email = sanitizeFormUsername($_POST['email']);

	$email2 = sanitizeFormUsername($_POST['email2']);

	$password = sanitizeFormPassword($_POST['password']);

	$password2 = sanitizeFormPassword($_POST['password2']);
	

}

?>


<!DOCTYPE html>
<html>
<head>
	<title>Welcome to Slotify</title>
</head>
<body>
	<div>
		<form>
			<h2>Login to your account</h2>
			<p>
				<label for="loginUsername">Username</label>
				<input id="loginUsername" type="text" placeholder="e.g. bartSimpson" name="loginUsername" required>
			</p>

			<p>
				<label for="loginPassword">Username</label>
				<input id="loginPassword" type="text" name="loginPassword" required>
			</p>

			<button type="submit" name="loginButton">Log IN</button>
		</form>
		<form>
			<h2>Create your account</h2>
			<p>
				<label for="username">Username</label>
				<input id="username" type="text" placeholder="e.g. bartSimpson" name="username" required>
			</p>

			<p>
				<label for="firstName">First Name</label>
				<input id="firstName" type="text" placeholder="e.g. Bart" name="firstName" required>
			</p>

			<p>
				<label for="LastName">Last Name</label>
				<input id="LastName" type="text" placeholder="e.g. Simpson" name="LastName" required>
			</p>

			<p>
				<label for="email">Email</label>
				<input id="email" type="email" placeholder="e.g. Bart@gmail.com" name="email" required>
			</p>

			<p>
				<label for="email2">Confirm Email</label>
				<input id="email2" type="email" placeholder="e.g. Bart@gmail.com" name="email2" required>
			</p>

			<p>
				<label for="password">Password</label>
				<input id="password" type="password" name="password" placeholder="Your Password" required>
			</p>
			<p>
				<label for="password2">Password</label>
				<input id="password2" type="password" name="password2" placeholder="Your Password" required>
			</p>
			<button type="submit" name="registerButton">Sign Up</button>
		</form>
	</div>
</body>
</html>