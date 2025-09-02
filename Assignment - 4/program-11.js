const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function classifyNumber() {
  let n = Number(await crw.get("Enter a number: "));

  let classification = 
    n >= 0 
      ? (Math.abs(n) < 100 
          ? (n % 2 === 0 ? "Small Positive Even" : "Small Positive Odd")
          : (n % 2 === 0 ? "Large Positive Even" : "Large Positive Odd")
        )
      : (Math.abs(n) < 100 
          ? (n % 2 === 0 ? "Small Negative Even" : "Small Negative Odd")
          : (n % 2 === 0 ? "Large Negative Even" : "Large Negative Odd")
        );

  return classification;
}

async function main() {
  const result = await classifyNumber();
  console.log(result);
  crw.close();
}

main();
