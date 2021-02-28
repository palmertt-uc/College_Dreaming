const emailRecipient = 'seniordesign908@gmail.com'
const emailSender = document.getElementById('emailInput');
const emailContent = document.getElementById('messageContent');
const contactPageSendEmail = document.getElementById('contact-page');

contactPageSendEmail.addEventListener('click', function () {

    let mailto_link = 'mailto:' + emailRecipient + '?subject=' + 'Email From '+ emailSender.value + ': ' + subject.value + '&body=' + emailContent.value;

    window = window.open(mailto_link, 'emailWindow');
    if (window && window.open && !window.closed) {
        window.close();
    }
});