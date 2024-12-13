const year = parseInt(prompt("Enter a year:"));

let isLeapYear = false;

if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    isLeapYear = true;
}

document.getElementById("tehtävä5").textContent = isLeapYear ? `${year} is a leap year.` : `${year} is not a leap year.`;
