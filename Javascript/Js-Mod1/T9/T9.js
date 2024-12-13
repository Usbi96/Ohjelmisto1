const number = parseInt(prompt("Enter an integer:"));
let isPrime = true;

if (number <= 1) {
    isPrime = false;
} else {
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            isPrime = false;
            break;
        }
    }
}

document.getElementById("tehtävä9").textContent = isPrime ? `${number} is a prime number.` : `${number} is not a prime number.`;
