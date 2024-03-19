
function validationCheck(event) { //function validates that form has been filled before submiting 
    var inputs = document.querySelectorAll(".input");
    var errorMessage= document.querySelectorAll(".error");
    var isvalid = true;
    // Example validation: Checking if both username and password are not empty
    for(let i=0; i<inputs.length; i++){
        if(inputs[i].value.trim() === ""){
            errorMessage[i].textContent = "Please enter a " + inputs[i].id;
            isvalid = false;
            event.preventDefault();
        }
    }
    if (!isvalid) {
        event.preventDefault(); // Prevent form submission
    } else {
        // Redirect to another page if validation passes
        window.location.href = "/link";
    }
 
    
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formLogin").addEventListener("submit", validationCheck)
    //clear error message if usesr tries again 
    document.getElementById("username").addEventListener("input", function() {
        document.getElementById("errorMessage").textContent = "";
    });
    document.getElementById("password").addEventListener("input", function() {
        document.getElementById("errorPassword").textContent = "";
    });
});



