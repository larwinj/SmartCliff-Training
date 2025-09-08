function sendEmail(callback) {
  console.log("Sending email...");

  setTimeout(() => {
    console.log("Email sent successfully");
    callback(); 
  }, 3000);
}

sendEmail(() => {
  console.log("Notification: User has been informed.");
});
