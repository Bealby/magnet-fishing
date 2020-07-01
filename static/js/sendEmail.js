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
            document.getElementById("demo").innerHTML = "Message Sent!";
            console.log("SUCCESS", response);
        
        },
        function(error) {
            document.getElementById("demo").innerHTML = "Message Failed";
            console.log("FAILED", error);
        }
    );

    return false;  // To block from loading a new page
}
