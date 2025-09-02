const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function smartElevator() {
  let floor = Number(await crw.get("Enter floor number: "));

  let maint = (await crw.get("Is maintenance mode on? (true/false): ")).trim().toLowerCase();
  let maintenance = maint === "true";

  let message;

  if (maintenance) {
    message = "Maintenance";
  } else {
    switch (true) {
      case (floor === 0):
        message = "Welcome";
        break;
      case (floor >= 1 && floor <= 5):
        message = "Go to Office";
        break;
      case (floor >= 6 && floor <= 9):
        message = "Go to Cafeteria";
        break;
      case (floor === 10):
        message = "Enjoy the view";
        break;
      default:
        message = "Invalid floor";
    }
  }

  return message;
}

async function main() {
  const result = await smartElevator();
  console.log(result);
  crw.close();
}

main();