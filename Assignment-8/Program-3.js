function safeJSONParse(str) {
  try {
    const parsed = JSON.parse(str); 
    return parsed;
  } catch (error) {
    return "Invalid JSON"; 
  }
}

let tc1 = '{"name":"Alice","age":25}';

console.log("Valid Input:", safeJSONParse(tc1));

let tc2 = '{name:"Alice",age:25}';
console.log("Invalid Input:", safeJSONParse(tc2));
