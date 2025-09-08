let transactions = [1000, 2000, -500, 3000];

const INR_TO_USD = 80;

let transactionsInUSD = transactions.map(amount => (amount / INR_TO_USD).toFixed(2));

console.log("Transactions in INR:", transactions);
console.log("Transactions in USD:", transactionsInUSD);