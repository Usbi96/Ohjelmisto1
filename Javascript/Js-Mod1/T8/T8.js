const startYear = parseInt(prompt("Enter the start year:"));
const endYear = parseInt(prompt("Enter the end year:"));
const leapYears = [];

for (let year = startYear; year <= endYear; year++) {
    if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
        leapYears.push(year);
    }
}

const outputElement = document.getElementById("tehtävä8");
leapYears.forEach(year => {
    const li = document.createElement("li");
    li.textContent = year;
    outputElement.appendChild(li);
});
