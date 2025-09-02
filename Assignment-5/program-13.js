const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

function getISOWeekNumber(dateStr) {
    let date = new Date(dateStr);

    // Copy date and set to nearest Thursday (current date + 4 - day number)
    let target = new Date(date.valueOf());
    let dayNr = (date.getDay() + 6) % 7; //Sun=0 → 6, Mon=1 → 0
    target.setDate(target.getDate() - dayNr + 3);

    // First Thursday of the year
    let firstThursday = new Date(target.getFullYear(), 0, 4);
    let firstDayNr = (firstThursday.getDay() + 6) % 7;
    firstThursday.setDate(firstThursday.getDate() - firstDayNr + 3);

    // Calculate week number
    let weekNumber = 1 + Math.round((target - firstThursday) / (7 * 24 * 60 * 60 * 1000));
    return weekNumber;
}

async function main() {
    let dateStr = await crw.get("Enter date (YYYY-MM-DD): ");
    let weekNo = getISOWeekNumber(dateStr);
    console.log(`ISO Week Number: ${weekNo}`);
    crw.close();
}

main();
