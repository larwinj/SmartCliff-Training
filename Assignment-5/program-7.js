const {consoleRW} = require('./consoleRW.js');
const crw = new consoleRW();

async function mergeIntervals(intervals){
    intervals.sort((a,b) => a[0] - b[0]);

    const merged = [];
    let prev = intervals[0];

    for(let i=1;i<intervals.length;i++){
        if(intervals[i][0] <= prev[1]){
            prev[1] = Math.max(prev[1],intervals[i][1]);
        }else{
            merged.push(prev);
            prev = intervals[i];
        }
    }
    merged.push(prev);
    return merged;
}

async function main(){
    let input = await crw.get("Enter a 2D array [[1,3],[2,4]]: ");
    const matrix = JSON.parse(input);
    const op = await mergeIntervals(matrix);
    console.log(op);
    crw.close();
}
main();