const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function calculateFare() {
  let age = Number(await crw.get("Enter age: "));
  let day = (await crw.get("Enter day: ")).trim().toLowerCase();

  let fareType;

  if (age < 5) {
    fareType = "Free";
  } else if (age >= 5 && age <= 17) {
    fareType = "Child Fare";
  } else if (age >= 18 && age <= 59) {
    fareType = "Adult Fare";
  } else {
    fareType = "Senior Fare";
  }

  if (day === "sunday") {
    if (fareType === "Free") {
      fareType += " (50% off applied → still Free)";
    } else {
      fareType += " (50% off)";
    }
  }

  return fareType;
}

async function main() {
  const result = await calculateFare();
  console.log(result);
  crw.close();
}

main();
