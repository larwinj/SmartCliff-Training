const {consoleRW} = require('./consoleRW.js');
const crw = new consoleRW();

async function spiralMatrix(matrix) {
    const res = [];
    let top = 0,bottom = matrix.length - 1;
    let left = 0,right = matrix[0].length - 1;

    while (top <= bottom && left <= right) {
        // Top row
        for (let i = left; i <= right; i++) {
            res.push(matrix[top][i]);
        }
        top++;

        // Right column
        for (let i = top; i <= bottom; i++) {
            res.push(matrix[i][right]);
        }
        right--;

        if (top <= bottom) {
            // Bottom row
            for (let i = right; i >= left; i--) {
                res.push(matrix[bottom][i]);
            }
            bottom--;
        }

        if (left <= right) {
            // Left column
            for (let i = bottom; i >= top; i--) {
                res.push(matrix[i][left]);
            }
            left++;
        }
    }
    return res;
}
async function main(){
    let input = await crw.get("Enter a 2D array [[1,2,3],[4,5,6],[7,8,9]]: ");
    const matrix = JSON.parse(input);
    const op = await spiralMatrix(matrix);
    console.log(op);
    crw.close();
}
main();