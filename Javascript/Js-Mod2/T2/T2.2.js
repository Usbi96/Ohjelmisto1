const numParticipants = parseInt(prompt("Enter the number of participants:"));
let participants = [];

for (let i = 0; i < numParticipants; i++) {
    participants.push(prompt(`Enter the name of participant ${i + 1}:`));
}

participants.sort();

const listElement = document.getElementById("tehtävä2.2");
participants.forEach(participant => {
    const li = document.createElement("li");
    li.textContent = participant;
    listElement.appendChild(li);
});
