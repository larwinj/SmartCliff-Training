const { consoleRW } = require("./consoleRW.js");
const crw = new consoleRW();

function getDiscountFunction(season) {
  if (season.toLowerCase() === "summer") {
    return (amount) => amount - (amount * 0.1);
  } else if (season.toLowerCase() === "winter") {
    return (amount) => amount - (amount * 0.2); 
  } else {
    return (amount) => amount;
  }
}

async function main() {
  let season = await crw.get("Enter season: ");
  let amount = parseFloat(await crw.get("Enter amount: "));

  const discountFunc = getDiscountFunction(season);
  const finalAmount = discountFunc(amount);

  console.log(`Original Amount: ₹${amount}`);
  console.log(`Final Amount after ${season} discount: ₹${finalAmount}`);

  crw.close();
}
main();
