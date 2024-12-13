let dogNames = [];

for (let i = 0; i < 6; i++) {
    dogNames.push(prompt(`Enter the name of dog ${i + 1}:`));
}

dogNames.sort().reverse();

const listElement = document.getElementById("tehtävä2.3");
dogNames.forEach(name => {
    const li = document.createElement("li");
    li.textContent = name;
    listElement.appendChild(li);
});
