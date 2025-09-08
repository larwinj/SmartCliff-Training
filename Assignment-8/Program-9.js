function fetchFlightStatus(flightNo) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (flightNo === "AI202") {
        resolve("Flight AI202 is On Time");
      } else if (flightNo === "AI404") {
        resolve("Flight AI404 is Delayed");
      } else {
        reject("Flight not found");
      }
    }, 2000);
  });
}

async function getFlightStatus(flightNo) {
  try {
    let status = await fetchFlightStatus(flightNo);
    console.log(status);
  } catch (error) {
    console.log(error);
  }
}

getFlightStatus("AI202"); 
getFlightStatus("AI404"); 
getFlightStatus("AI999"); 