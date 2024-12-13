const numDice = parseInt(prompt("Enter the number of dice rolls:"));
const targetSum = parseInt(prompt("Enter the target sum:"));
const trials = 10000;
let count = 0;

for (let i = 0; i < trials; i++) {
    let sum = 0;
    for (let j = 0; j < numDice; j++) {
        sum += Math.floor(Math.random() * 6) + 1;
    }
    if (sum === targetSum) {
        count++;
    }
}

const probability = (count / trials) * 100;
document.getElementById("tehtävä10").textContent = `Probability to get sum ${targetSum} with ${numDice} dice is ${probability.toFixed(2)}%`;
