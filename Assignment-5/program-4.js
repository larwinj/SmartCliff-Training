const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function func(){
    let input = await crw.get("Enter an array[1,2,3,4]: ");
    
    let arr = JSON.parse(input);
    let n = arr.length;
    let p = 1;
    for(let i=0;i<n;i++){
        p*=arr[i];
    }

    const res = [];
    for(let i=0;i<n;i++){
        res.push(p/arr[i]);
    }
    return res;
}

async function main(){
    const op = await func();
    console.log(op);
    crw.close();
}
main();