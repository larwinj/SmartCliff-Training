const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function processStudentResult() {
  let input = await crw.get("Enter student marks {math:90,science:80}): ");
  
  let marks;
  try {
    marks = JSON.parse(input.replace(/(\w+):/g, '"$1":'));
  } catch (e) {
    return "Invalid input format!";
  }

  let total = 0;
  let count = 0;
  let hasFail = false;

  for (let subject in marks) {
    let mark = marks[subject];
    if (mark < 35) {
      hasFail = true;
      break; //stop
    }
    total += mark;
    count++;
  }

  if (hasFail) {
    return "Fail (due to <35 in a subject)";
  }

  let average = total / count;

  if (average >= 75) {
    return "Distinction";
  } else if (average >= 50 && average <= 74) {
    return "Pass";
  } else {
    return "Fail";
  }
}

async function main() {
  const result = await processStudentResult();
  console.log(result);
  crw.close();
}

main();
