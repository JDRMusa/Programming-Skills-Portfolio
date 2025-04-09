// First, get the variables or in this case, constant
const priceChosen = document.getElementById('price');
const amountChosen = document.getElementById('amount');
const calculateButton = document.getElementById('calculateButton');
const totalCostDisplay = document.getElementById('totalCost');

// Then create a function to calculate the total cost
function calculateTotal() {
  const price = parseFloat(priceChosen.value); // Get the price per liter
  const amount= parseFloat(amountChosen.value); // Get the number of liters purchased
  
  // This is for error handling
  if (isNaN(price) || isNaN(amount) || price < 0 || amount < 0) {
    alert('Please enter valid positive numbers for both fields.');
    return;
  }

  // A variable named totalCost to do the basic calculation for the total
  const totalCost = price * amount;

  // This will display the cost got by the totalCost constant and displayed
  totalCostDisplay.textContent = `Total Cost: ${totalCost.toFixed(2)}`;
}

// This is to make the calculateTotal function work on click of the calculateButton
calculateButton.addEventListener('click', calculateTotal);