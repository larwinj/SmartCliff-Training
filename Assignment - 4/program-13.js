const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function calculateDiscount() {
  let cartValue = Number(await crw.get("Enter cart value (₹): "));
  let customerType = (await crw.get("Enter customer type (Normal/Premium): ")).trim().toLowerCase();
  let day = (await crw.get("Enter day: ")).trim().toLowerCase();

  let discount = 0;

  if (day === "black friday") {
    discount = 50;
  } else {
    if (cartValue > 10000) {
      discount = 20;
    } else if (cartValue >= 5000 && cartValue <= 9999) {
      discount = 10;
    } else if (cartValue < 5000 && customerType === "premium") {
      discount = 5;
    } else {
      discount = 0;
    }
  }

  return `Discount applied: ${discount}%`;
}

async function main() {
  const result = await calculateDiscount();
  console.log(result);
  crw.close();
}

main();
