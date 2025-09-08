const services = {
  "Oil Change": { price: 1500, time: 3000 },
  "Tire Replacement": { price: 4000, time: 5000 },
  "Engine Check": { price: 2500, time: 4000 },
  "Full Service": { price: 7000, time: 7000 }
};

document.getElementById("serviceForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const customer = {
    name: document.getElementById("name").value,
    vehicleType: document.getElementById("vehicleType").value,
    model: document.getElementById("model").value,
    contact: document.getElementById("contact").value,
    service: document.getElementById("service").value
  };

  const { price, time } = services[customer.service];

  const statusDiv = document.getElementById("status");
  const billDiv = document.getElementById("bill");

  statusDiv.innerHTML = "";
  billDiv.innerHTML = "";

  async function processService() {
    statusDiv.innerHTML = "Status: Booked";

    await new Promise(res => setTimeout(res, 2000));
    statusDiv.innerHTML = "Status: In Progress...";

    await new Promise(res => setTimeout(res, time));
    statusDiv.innerHTML = "Status: Completed";

    generateBill(customer, price);
  }

  function generateBill({ name, vehicleType, model, contact, service }, price) {
    billDiv.innerHTML = `
      <h3>🧾 Final Bill</h3>
      <p><b>Customer:</b> ${name}</p>
      <p><b>Vehicle:</b> ${vehicleType} - ${model}</p>
      <p><b>Contact:</b> ${contact}</p>
      <p><b>Service:</b> ${service}</p>
      <p><b>Total Amount:</b> ₹${price}</p>
    `;
  }

  processService();
});
