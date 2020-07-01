function sendMail(contactForm) {
    emailjs.init("user_ltp9VN3EuB6AFgRZdXukW");
    emailjs.send("gmail", "magnet_fishing", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "comment": contactForm.comment.value
    })
    .then(
        function(response) {
        document.getElementById("myForm").reset();
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );

    return false;  // To block from loading a new page
}

/*
//NEW SEND CODE
// code fragment
// the form id is myForm
$('#myForm').on('submit', function(event) {
    event.preventDefault(); // prevent reload
    
    var formData = new FormData(this);
    formData.append('service_id', 'gmail');
    formData.append('template_id', 'magnet-fishing');
    formData.append('user_id', 'user_ltp9VN3EuB6AFgRZdXukW');
 
    $.ajax('https://api.emailjs.com/api/v1.0/email/send-form', {
        type: 'POST',
        data: formData,
        contentType: false, // auto-detection
        processData: false // no need to parse formData to string
    }).done(function() {
        alert('Your mail is sent!');
    }).fail(function(error) {
        alert('Oops... ' + JSON.stringify(error));
    });
});
// code fragment
*/