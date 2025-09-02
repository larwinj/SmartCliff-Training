const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function findDayOfWeek() {
    let dateStr = await crw.get("Enter a date (YYYY-MM-DD): ");
    let date = new Date(dateStr);

    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    let dayName = days[date.getDay()];

    console.log(`Day of the week: ${dayName}`);
}

async function main() {
    await findDayOfWeek();
    crw.close();
}

main();
