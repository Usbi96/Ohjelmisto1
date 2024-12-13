function rollDice(sides) {
    return Math.floor(Math.random() * sides) + 1;
}

const sides = parseInt(prompt("Enter the number of sides on the dice:"));
let result;
let rolls = [];

do {
    result = rollDice(sides);
    rolls.push(result);
} while (result !== sides);

const listElement = document.getElementById("tehtävä2.7");
rolls.forEach(roll => {
    const li = document.createElement("li");
    li.textContent = roll;
    listElement.appendChild(li);
});
