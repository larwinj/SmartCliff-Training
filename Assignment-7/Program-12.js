function* fetchData(totalItems = 30, pageSize = 10) {
  let currentPage = 0;

  while (currentPage * pageSize < totalItems) {
    const start = currentPage * pageSize + 1;
    const end = Math.min(start + pageSize - 1, totalItems);

    let pageData = [];
    for (let i = start; i <= end; i++) {
      pageData.push(i);
    }

    yield pageData;
    currentPage++;
  }
}

let data = fetchData(30, 10);

console.log(data.next().value); 
console.log(data.next().value); 
console.log(data.next().value); 
console.log(data.next().value);