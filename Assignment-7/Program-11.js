function moviePlaylist(movies) {
  let index = 0;

  return {
    next: function() {
      if (index < movies.length) {
        return { value: movies[index++], done: false };
      } else {
        return { done: true };
      }
    }
  };
}

let playlist = moviePlaylist(["Avengers", "Inception"]);

console.log(playlist.next());
console.log(playlist.next());
console.log(playlist.next());