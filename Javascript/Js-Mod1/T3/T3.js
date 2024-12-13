const num1 = parseInt(prompt("Enter the first num:"), 10);
const num2 = parseInt(prompt("Enter the second num:"), 10);
const num3 = parseInt(prompt("Enter the third num:"), 10);

const sum = num1 + num2 + num3;
const product = num1 * num2 * num3;
const average = sum / 3;

document.getElementById("tehtävä3").innerHTML = `
    Sum: ${sum}<br>
    Product: ${product}<br>
    Average: ${average}
`;
