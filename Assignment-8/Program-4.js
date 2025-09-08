function verifyUser() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      let isLoggedIn = true;
      if (isLoggedIn) {
        resolve("User verified");
      } else {
        reject("User not logged in");
      }
    }, 1000);
  });
}

function processPayment() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      let paymentSuccess = true; 
      if (paymentSuccess) {
        resolve("Payment processed");
      } else {
        reject("Payment failed");
      }
    }, 1000);
  });
}

function confirmOrder() {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve("Order confirmed");
    }, 1000);
  });
}

verifyUser()
  .then((msg) => {
    console.log(msg);
    return processPayment(); 
  })
  .then((msg) => {
    console.log(msg);
    return confirmOrder(); 
  })
  .then((msg) => {
    console.log(msg); 
  })
  .catch((err) => {
    console.error("Error:", err); 
  });
