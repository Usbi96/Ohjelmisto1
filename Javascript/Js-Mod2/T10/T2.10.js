const numCandidates = parseInt(prompt("Enter the number of candidates:"));
let candidates = [];
for (let i = 0; i < numCandidates; i++) {
    const candidateName = prompt(`Enter the name for candidate ${i + 1}:`);
    candidates.push({ name: candidateName, votes: 0 });
}
const numVoters = parseInt(prompt("Enter the number of voters:"));

for (let i = 0; i < numVoters; i++) {
    const vote = prompt(`Voter ${i + 1}, who will you vote for? (Enter the candidate's name or leave empty for no vote):`);

    if (vote !== "") {
        const candidate = candidates.find(c => c.name.toLowerCase() === vote.toLowerCase());
        if (candidate) {
            candidate.votes += 1;
        }
    }
}

candidates.sort((a, b) => b.votes - a.votes);
const winner = candidates[0];
console.log(`The winner is ${winner.name} with ${winner.votes} votes.`);

console.log("Results:");
candidates.forEach(candidate => {
    console.log(`${candidate.name}: ${candidate.votes} votes`);
});
