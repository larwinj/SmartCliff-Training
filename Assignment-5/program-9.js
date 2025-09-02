const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

function addBigIntegers(num1, num2) {
    let i = num1.length - 1;
    let j = num2.length - 1;
    let carry = 0;
    let result = "";

    while (i >= 0 || j >= 0 || carry) {
        let digit1 = i >= 0 ? parseInt(num1[i]) : 0;
        let digit2 = j >= 0 ? parseInt(num2[j]) : 0;

        let sum = digit1 + digit2 + carry;
        result = (sum % 10) + result;
        carry = Math.floor(sum / 10);

        i--;
        j--;
    }

    return result;
}

async function main() {
    let num1 = await crw.get("Enter first big integer: ");
    let num2 = await crw.get("Enter second big integer: ");

    const sum = addBigIntegers(num1, num2);
    console.log("Sum:", sum);

    crw.close();
}

main();
