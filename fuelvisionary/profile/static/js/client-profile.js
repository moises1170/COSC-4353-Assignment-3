document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('full-name').setAttribute('maxlength', '50');
    document.getElementById('address1').setAttribute('maxlength', '100');
    document.getElementById('address2').setAttribute('maxlength', '100');
    document.getElementById('city').setAttribute('maxlength', '100');
    document.getElementById('zip').setAttribute('maxlength', '9');
});



document.getElementById('profile-form').addEventListener('submit', function(event) {
    var zipCode = document.getElementById('zip').value;
    if (zipCode.length < 5) {
        event.preventDefault();
        alert('ZIP code must be at least 5 characters.');
    }
});