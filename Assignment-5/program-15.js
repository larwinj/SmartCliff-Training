const { consoleRW } = require("./consoleRW.js");
const crw = new consoleRW();

function extractNumbers(text) {
    const regex = /-?\d+(\.\d+)?/g;
    const matches = text.match(regex);

    return matches ? matches.map(Number) : [];
}

async function main() {
    let inputText = await crw.get("Enter text: ");
    const numbers = extractNumbers(inputText);
    console.log("Extracted Numbers:", numbers);
    crw.close();
}

main();
