const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function Subarray_Sum_k(){
    let input = await crw.get("Enter an array[1,2,3,4]: ");
    let k = parseInt(await crw.get("Enter k: "));
    let nums = JSON.parse(input);
    let n = nums.length;
    const sum = new Array(n);
    sum[0] = nums[0];

    for(let i=1;i<n;i++){
        sum[i] = sum[i-1] + nums[i];
    }
    let count = 0;
    for(let i=0;i<n;i++){
        if(sum[i] === k) count++;
        for(let j=0;j<i;j++){
            if(sum[i] - sum[j] === k) count++;
        }
    }
    return count;
} 
async function main(){
    const op = await Subarray_Sum_k();
    console.log(op);
    crw.close();
}
main();