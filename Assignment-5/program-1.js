const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function generate(){
    let str = await crw.get("Enter a String: ");
    let num = 1;
    let res = "";

    for (let i = 1; i < str.length; i++) {
        if (str[i] === str[i - 1]) {
            num++;
        } else {
            res += str[i - 1] + num;
            num = 1;
        }
    }
    res += str[str.length - 1] + num;
    return res;
}

async function main(){
    const op = await generate();
    console.log(op);
    crw.close();
}

main();
