const numDice = parseInt(prompt("Enter the number of dice rolls:"));
let sum = 0;

for (let i = 0; i < numDice; i++) {
    sum += Math.floor(Math.random() * 6) + 1;
}

document.getElementById("tehtävä7").textContent = `The sum of the dice rolls is: ${sum}`;
