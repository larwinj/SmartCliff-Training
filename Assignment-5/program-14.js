const { consoleRW } = require("./consoleRW.js");
const crw = new consoleRW();

function isStrongPassword(password) {
    const strongRegex = /^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[^A-Za-z0-9]).{8,}$/;
    return strongRegex.test(password);
}

async function main() {
    let pwd = await crw.get("Enter password: ");
    console.log("Strong Password:", isStrongPassword(pwd));
    crw.close();
}

main();
