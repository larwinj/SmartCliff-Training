const { consoleRW } = require("./consoleRW.js");
const crw = new consoleRW();

function getWeather(city) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (city === "Chennai") {
        resolve(`Sunny in ${city}`);
      } else {
        reject("City not found");
      }
    }, 1000);
  });
}

async function func() {
  const city = await crw.get("Enter city name: ");
  try {
    const response = await getWeather(city);
    console.log("Success:", response);
    
  } catch (error) {
    console.log("Error:", error);
  }finally{
    crw.close();
  }
}

func();