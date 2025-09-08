let employees = [ 
  { name: "A", salary: 60000 }, 
  { name: "B", salary: 40000 }, 
  { name: "C", salary: 25000 }, 
  { name: "D", salary: 50000 }, 
  { name: "E", salary: 30000 } 
];
let highEarners = employees.filter(emp => emp.salary > 50000);

let mediumEarners = employees.filter(emp => emp.salary >= 30000 && emp.salary <= 50000);

let lowEarners = employees.filter(emp => emp.salary < 30000);

console.log("High Earners:", highEarners);
console.log("Medium Earners:", mediumEarners);
console.log("Low Earners:", lowEarners);
