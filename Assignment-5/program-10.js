const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

function isArmstrong(num) {
    let temp = num;
    let digits = 0;

    while (temp > 0) {
        digits++;
        temp = Math.floor(temp / 10);
    }

    temp = num;
    let sum = 0;

    while (temp > 0) {
        let digit = temp % 10;
        sum += digit ** digits;
        temp = Math.floor(temp / 10);
    }

    return sum === num;
}

async function main() {
    let input = await crw.get("Enter a number: ");
    let num = parseInt(input);

    if (isNaN(num)) {
        console.log("Invalid input! Please enter a valid number.");
    } else {
        console.log("Is Armstrong Number?", isArmstrong(num));
    }

    crw.close();
}

main();
