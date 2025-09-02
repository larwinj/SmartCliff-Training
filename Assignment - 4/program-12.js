let states = ["Green", "Yellow", "Red"];
let cycleCount = 0;
let maxCycles = 5;
let index = 0;

while (true) {
  let currentState = states[index];

  switch (currentState) {
    case "Green":
      console.log("Green → Cars move");
      break;
    case "Yellow":
      console.log("Yellow → Prepare to stop");
      break;
    case "Red":
      console.log("Red → Stop");
      break;
  }

  index = (index + 1) % states.length;

  if (index === 0) {
    cycleCount++;
    if (cycleCount === maxCycles) {
      console.log("Stopped after 5 cycles");
      break;
    }
  }
}
