const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function numberGuessingGame() {
  const secret = 5; // fixed secret number
  let guess;

  do {
    guess = Number(await crw.get("Guess a number between 1 and 10: "));
    if (guess !== secret) {
      console.log("Wrong guess, try again!");
    }
  } while (guess !== secret);

  console.log("🎉 Correct! The secret number was " + secret);
}

async function main() {
  await numberGuessingGame();
  crw.close();
}

main();
