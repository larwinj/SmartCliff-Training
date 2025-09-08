let personalInfo = { name: "Alice", age: 25 };

let jobInfo = { role: "Developer", salary: 60000 };

let employee = { ...personalInfo, ...jobInfo };

console.log(employee);