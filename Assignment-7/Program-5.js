const { consoleRW } = require("./consoleRW.js");
const crw = new consoleRW();

function createLogger(type) {
    return function(message) {
        console.log(`[${type.toUpperCase()}] ${message}`);
    }
}

async function main() {

  const errorLogger = createLogger("error");
  const infoLogger = createLogger("info");

  let choice = await crw.get("Choose log type (error/info): ");
  let message = await crw.get("Enter your message: ");

  if (choice.toLowerCase() === "error") {
    errorLogger(message);
  } else if (choice.toLowerCase() === "info") {
    infoLogger(message);
  } else {
    console.log("[UNKNOWN] Invalid log type entered.");
  }

  crw.close();
}

main();
