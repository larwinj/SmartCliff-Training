const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function filterWords() {

  let wordsInput = await crw.get("Enter words separated by commas: ");
  let words = wordsInput.split(",").map(w => w.trim());

  let n = Number(await crw.get("Enter minimum length n: "));

  let result = words.filter(word => word.length >= n);

  return result.join(", ");
}

async function main() {
  const result = await filterWords();
  console.log("Filtered Words: " + result);
  crw.close();
}

main();