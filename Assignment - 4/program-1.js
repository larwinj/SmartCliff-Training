outerLoop: for (let row = 0; row < 8; row++) {
  for (let col = 0; col < 8; col++) {
    // Check if square is black
    if ((row + col) % 2 === 0) {
      console.log(`(${row}, ${col})`);
    }

    if (row === 5 && col === 5) {
      console.log("Stopped at (5,5)");
      break outerLoop;
    }
  }
}
