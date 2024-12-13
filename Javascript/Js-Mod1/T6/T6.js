if (confirm("Should I calculate the square root?")) {
    const number = parseFloat(prompt("Enter a number:"));
    if (number < 0) {
        document.getElementById("tehtävä6").textContent = "The square root of a negative number is not defined.";
    } else {
        document.getElementById("tehtävä6").textContent = `The square root is: ${Math.sqrt(number)}`;
    }
} else {
    document.getElementById("tehtävä6").textContent = "The square root is not calculated.";
}
