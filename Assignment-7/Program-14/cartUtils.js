export function addToCart(cart, item) {
  cart.push(item);
  console.log(`${item.name} added to cart.`);
  return cart;
}

export function calculateTotal(cart) {
  let total = cart.reduce((sum, item) => sum + item.price, 0);
  return total;
}

export function applyDiscount(total, discountPercentage) {
  let discounted = total - (total * discountPercentage) / 100;
  return discounted;
}
