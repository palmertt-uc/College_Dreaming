// Contact Page information
const sendEmail = document.getElementById('contact');
const emailRecipient = 'seniordesign908@gmail.com'

// Button For Sending Email
sendEmail.addEventListener('click', function () {

    let mailto_link = 'mailto:' + emailRecipient;

    window = window.open(mailto_link, 'emailWindow');
    if (window && window.open && !window.closed) {
        window.close();
    }
});