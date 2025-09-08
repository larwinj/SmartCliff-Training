import { addToCart, calculateTotal, applyDiscount } from "./cartUtils.js";

let cart = [];

addToCart(cart, { name: "Laptop", price: 50000 });
addToCart(cart, { name: "Phone", price: 20000 });
addToCart(cart, { name: "Headphones", price: 5000 });

let total = calculateTotal(cart);
console.log("Total before discount:", total);

let finalPrice = applyDiscount(total, 10);
console.log("Total after 10% discount:", finalPrice);