let orders = [
  {
    id: 1,
    customer: "Alice",
    items: [
      { name: "Laptop", price: 50000 },
      { name: "Mouse", price: 1000 }
    ],
    status: "delivered"
  },
  {
    id: 2,
    customer: "Bob",
    items: [
      { name: "Phone", price: 20000 },
      { name: "Earphones", price: 1500 }
    ],
    status: "pending"
  },
  {
    id: 3,
    customer: "Charlie",
    items: [
      { name: "Tablet", price: 30000 }
    ],
    status: "delivered"
  }
];

let customers = orders.map(order => order.customer);
console.log("Customers:", customers);

let deliveredOrders = orders.filter(order => order.status === "delivered");
console.log("Delivered Orders:", deliveredOrders);

let totalRevenue = orders.reduce((sum, order) => {
  let orderTotal = order.items.reduce((itemSum, item) => itemSum + item.price, 0);
  return sum + orderTotal;
}, 0);
console.log("Total Revenue:", totalRevenue);

orders.forEach(order => {
  console.log(`Order ID: ${order.id}, Customer: ${order.customer}, Status: ${order.status}`);
});
