const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function atmSimulation() {
  let balance = 10000;

  console.log("Welcome to the ATM!");
  console.log("Available operations: Deposit, Withdraw, Balance, Exit");

  while (true) {
    let input = (await crw.get("Enter operation: ")).trim().toLowerCase();

    if (input === "exit") {
      console.log("Exiting...");
      break;
    }

    switch (input) {
      case "deposit":
        let depositAmount = Number(await crw.get("Enter amount to deposit: "));
        if (depositAmount <= 0) {
          console.log("Invalid deposit amount.");
          continue;
        }
        balance += depositAmount;
        console.log(`Deposited ₹${depositAmount}. New balance: ₹${balance}`);
        break;

      case "withdraw":
        let withdrawAmount = Number(await crw.get("Enter amount to withdraw: "));
        if (withdrawAmount <= 0) {
          console.log("Invalid withdrawal amount.");
          continue;
        }
        if (withdrawAmount > balance) {
          console.log("Insufficient balance!");
          continue;
        }
        balance -= withdrawAmount;
        console.log(`Withdrew ₹${withdrawAmount}. Remaining balance: ₹${balance}`);
        break;

      case "balance":
        console.log(`Current balance: ₹${balance}`);
        break;

      default:
        console.log("Invalid operation. Try again.");
        continue;
    }
  }
}

async function main() {
  await atmSimulation();
  crw.close();
}

main();
