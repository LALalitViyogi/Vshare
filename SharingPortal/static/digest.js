function hashPassword() {
  let password = document.getElementById('password');
  if(password.value.length<8){
    alert("Password must have atleast 8 characters");
  }
  else{
    var sha256 = new CryptoJS.SHA256(password.value);
    document.getElementById('password').value =sha256.toString();
  }
}

function validateEmail(email) {
  // Regular expression for validating email addresses
  var regex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;

  // If the email address does not match the regular expression, return false
  if (!regex.test(email)) {
    return false;
  }

  // Otherwise, return true
  return true;
}

function manageEmail(){
  let email = document.getElementById('email');
  if(!(validateEmail(email.value))){
    alert("Enter Valid Email id");
  }
}