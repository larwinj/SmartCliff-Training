const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function validParentheses(){
    let str = await crw.get("Enter a String of Parentheses: ");
    let lb = 0,rb = 0;
    for(let i=0;i<str.length;i++){
        if(str[i] === '('){
            lb++;
            rb++;
        }else if(str[i] === ')'){
            lb--;
            rb--;
        }else{
            lb--;
            rb++;
        }
        if(lb < 0) lb = 0;
        if(rb < 0) return false;
    }
    return lb === 0;
}
async function main(){
    const op = await validParentheses();
    console.log(op);
    crw.close();
}
main();