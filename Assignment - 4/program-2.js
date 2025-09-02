const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function categorizeStatus() {
  let category;
  let code = Number(await crw.get("Enter HTTP status code: "));

  switch (true) {
    case (code >= 200 && code <= 299):
      category = "Success";
      break;
    case (code >= 300 && code <= 399):
      category = "Redirect";
      break;
    case (code >= 400 && code <= 499):
      category = "Client Error";
      break;
    case (code >= 500 && code <= 599):
      category = "Server Error";
      break;
    default:
      category = "Invalid Code";
  }
  return category;
}

async function main() {
  const result = await categorizeStatus();
  console.log(result);
  crw.close();
}

main();