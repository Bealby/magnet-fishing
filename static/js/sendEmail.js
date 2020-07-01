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
            swal("Message Sent!", "I'll be in touch soon!", "success");
            console.log("SUCCESS", response);
        
        },
        function(error) {
            swal("Message Failed!", "Error___please check connection and try again", "error");
            console.log("FAILED", error);
        }
    );

    return false;  // To block from loading a new page
}
