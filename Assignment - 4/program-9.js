const { consoleRW } = require('./consoleRW.js');
const crw = new consoleRW();

async function checkSubmission() {
  let time = Number(await crw.get("Enter time left (minutes): "));
  let answered = Number(await crw.get("Enter number of questions answered: "));
  let submittedInput = (await crw.get("Has the exam been submitted? (true/false): ")).trim().toLowerCase();
  let submitted = submittedInput === "true";

  let result;

  if (time <= 0) {
    result = "Submission Failed: No time left";
  } else if (answered < 1) {
    result = "Submission Failed: No answers";
  } else if (submitted) {
    result = "Submission Failed: Already submitted";
  } else {
    result = "Submission Accepted";
  }

  return result;
}

async function main() {
  const result = await checkSubmission();
  console.log(result);
  crw.close();
}

main();
