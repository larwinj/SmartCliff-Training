const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function longestSubstring() {
    let str = await crw.get("Enter a String: ");
    let maxLen = 0;
    const set = new Set();
    let left = 0;

    for(let right = 0; right < str.length; right++) {
        while(set.has(str[right])) {
            set.delete(str[left]);
            left++;
        }
        set.add(str[right]);
        maxLen = Math.max(maxLen, right - left + 1);
    }

    return maxLen;
}
async function main(){
    const op = await longestSubstring();
    console.log(op);
    crw.close();
}
main();