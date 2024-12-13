let numbers = [];
let input;

while (true) {
    input = parseInt(prompt("Enter a number:"));
    if (numbers.includes(input)) {
        alert("This number has already been given.");
        break;
    }
    numbers.push(input);
}

numbers.sort((a, b) => a - b);
console.log(numbers);
