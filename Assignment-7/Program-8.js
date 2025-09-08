function countVotes(candidate, ...votes) {
  let count = votes.filter(vote => vote === candidate).length;
  console.log(`${candidate} received ${count} votes`);
}

countVotes("Alice", "Alice", "Bob", "Alice");

countVotes("Bob", "Alice", "Bob", "Charlie", "Bob", "Bob");