function validateScores(scores) {
  let result = "All OK";

  outerLoop: for (let i = 0; i < scores.length; i++) {
    for (let j = 0; j < scores[i].length; j++) {
      if (scores[i][j] < 35) {
        result = `Failing score found at coordinate (${i},${j})`;
        break outerLoop;
      }
    }
  }

  return result;
}

console.log(validateScores([[60, 70], [80, 90]]));
console.log(validateScores([[60, 34], [80, 90]]));
console.log(validateScores([[45, 55], [20, 99]])); 
