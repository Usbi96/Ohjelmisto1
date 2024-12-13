function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

let result;
let rolls = [];

do {
    result = rollDice();
    rolls.push(result);
} while (result !== 6);

const listElement = document.getElementById("tehtävä2.6");
rolls.forEach(roll => {
    const li = document.createElement("li");
    li.textContent = roll;
    listElement.appendChild(li);
});
