function generateSalarySlip(employee) {
  const { name, salary, role = "Not Assigned" } = employee;

  return `Employee: ${name} | Role: ${role} | Salary: $${salary}`;
}

let emp1 = { name: "Alice", salary: 60000, role: "Developer" };
let emp2 = { name: "Bob", salary: 45000 };

console.log(generateSalarySlip(emp1));

console.log(generateSalarySlip(emp2));
