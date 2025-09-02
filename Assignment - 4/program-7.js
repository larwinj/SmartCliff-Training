function mazeEscape(grid) {
  const rows = grid.length;
  const cols = grid[0].length;

  let escaped = false;
  let i = 0, j = 0;
  outerLoop: while (true) {
    
    if (i === rows - 1 && j === cols - 1 && grid[i][j] === 0) {
      escaped = true;
      break outerLoop;
    }

    if (j + 1 < cols && grid[i][j + 1] === 0) {
      j++;
    }
    
    else if (i + 1 < rows && grid[i + 1][j] === 0) {
      i++;
    }
    
    else {
      break outerLoop;
    }
  }

  return escaped ? "Escaped" : "Blocked";
}

console.log(mazeEscape([[0,0,1],[1,0,0],[1,0,0]]));
console.log(mazeEscape([[0,1],[1,0]]));
console.log(mazeEscape([[0,0,0],[0,1,0],[0,0,0]]));
