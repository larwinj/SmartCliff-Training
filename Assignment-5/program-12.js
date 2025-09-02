const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

function addBusinessDays(dateStr, n) {
    let date = new Date(dateStr);

    while (n > 0) {
        // move to next day
        date.setDate(date.getDate() + 1);

        let day = date.getDay();
        if (day !== 0 && day !== 6) {
            n--; // count only weekdays
        }
    }
    return date.toISOString().split("T")[0]; // return YYYY-MM-DD
}

async function main() {
    let dateStr = await crw.get("Enter start date (YYYY-MM-DD): ");
    let n = parseInt(await crw.get("Enter business days to add: "));

    let result = addBusinessDays(dateStr, n);
    console.log(`Resulting date: ${result}`);

    crw.close();
}

main();
