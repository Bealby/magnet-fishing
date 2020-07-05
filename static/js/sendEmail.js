// Script for EmailJS API as well as alerts
// Environ variable set up for EMAILJS_KEY

function sendMail(contactForm) {
    emailjs.send("gmail", "magnet_fishing", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "comment": contactForm.comment.value
    })
    .then(
        function(response) {
            document.getElementById("myForm").reset();  // Clears contact form after message sent
            swal("Message Sent", "We will be in touch soon!", "success"); // Message Alert for 'Message Sent'
            console.log("SUCCESS", response);
        
        },
        function(error) {
            swal("Message Fail", "Please check connection and try again", "error"); // Message Alert for 'Message Fail'
            console.log("FAILED", error);
        }
    );

    return false;  // To block from loading a new page
}
