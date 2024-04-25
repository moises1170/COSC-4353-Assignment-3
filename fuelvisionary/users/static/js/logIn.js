
function validationCheck(event) { //function validates that form has been filled before submiting 
    var inputs = document.querySelectorAll(".input");
    var errorMessage= document.querySelectorAll(".error");
    var email = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var isvalid = true;
    // Example validation: Checking if both username and password are not empty
    for(let i=0; i<inputs.length; i++){
        if(inputs[i].value.trim() === ""){
            errorMessage[i].textContent = "Please enter a " + inputs[i].id;
            isvalid = false;
            event.preventDefault();
        }
    }
    // Example validation: Checking if email is valid  
    if (!validateEmail(email) && email.trim() !== ""){
        document.getElementById("errorMessage").textContent = "Please enter a valid email";
        isvalid = false;
    }
    if(password.length < 8 && password.trim() !== ""){
        document.getElementById("errorPassword").textContent = "Password must be at least 8 characters";
        isvalid = false;
    }
    
    if (!isvalid) {
        event.preventDefault(); // Prevent form submission
    } else {
        // Redirect to another page if validation passes
        window.location.href = "/link";
    }
 
    
    }
    function validateEmail(email) {
        var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return regex.test(email);
    }

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formLogin").addEventListener("submit", validationCheck)
    //clear error message if usesr tries again 
    document.getElementById("username").addEventListener("input", function() {
        var errors = document.querySelectorAll(".error")
        for(var error of errors){
            error.textContent="";
        }
    
    });
    document.getElementById("password").addEventListener("input", function() {
        var errors = document.querySelectorAll(".error")
        for(var error of errors){
            error.textContent="";
        }
    
    });
   


});



