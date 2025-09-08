const { consoleRW } = require("./consoleRW.js");
const crw = new consoleRW();

function bookRoom(type = "Standard", nights = 1) {
    if (type.toLowerCase() !== "Standard".toLowerCase() && type.toLowerCase() !== "Deluxe".toLowerCase()) {
        console.log("Invalid room type. Choose 'Standard' or 'Deluxe'.");
        return;
    }
  console.log(`Room booked: ${type} for ${nights} night(s)`);
}

async function main() {
  let type = await crw.get("Enter room type (Standard/Deluxe) [default: Standard]: ");
  let nights = await crw.get("Enter number of nights [default: 1]: ");

  type = type.trim() === "" ? "Standard" : type;
  nights = nights.trim() === "" ? 1 : parseInt(nights);

  bookRoom(type, nights);

  crw.close();
}

main();
