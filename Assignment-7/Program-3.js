const { consoleRW } = require("./consoleRW.js");
const crw = new consoleRW();

function sortStudents(students, comparator) {
  return students.sort(comparator);
}

async function main() {
  let students = [
    { name: "Alice", marks: 80 },
    { name: "Bob", marks: 60 },
    { name: "Charlie", marks: 90 }
  ];

  console.log("Original Students List:");
  console.log(students);

  let choice = await crw.get("Sort by 'name' or 'marks'? ");

  let sorted;
  if (choice.toLowerCase() === "marks") {
    sorted = sortStudents(students, (a, b) => a.marks - b.marks);
  } else if (choice.toLowerCase() === "name") {
    sorted = sortStudents(students, (a, b) => a.name.localeCompare(b.name));
  } else {
    console.log("Invalid choice! Please type 'name' or 'marks'.");
    crw.close();
    return;
  }

  console.log("Sorted Students:");
  console.log(sorted);

  crw.close();
}

main();
