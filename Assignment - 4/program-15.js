const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function airlineCheckIn() {
  let vipInput = (await crw.get("Is passenger VIP?")).trim().toLowerCase();
  let vip = vipInput === "true";

  let travelClass = (await crw.get("Enter class (Business/Economy): ")).trim().toLowerCase();
  let baggage = Number(await crw.get("Enter baggage weight (kg): "));

  let message = "";

  if (vip) {
    message = "Priority Check-in";
  } else {
    switch (travelClass) {
      case "business":
        message = "Priority Check-in";
        break;
      case "economy":
        message = "Normal Check-in";
        break;
      default:
        message = "Invalid class";
    }
  }

  if (baggage > 30) {
    message += " + Excess Baggage Fee";
  }

  return message;
}

async function main() {
  const result = await airlineCheckIn();
  console.log(result);
  crw.close();
}

main();
