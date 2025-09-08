class NoAnswerError extends Error {
  constructor(message) {
    super(message);
    this.name = "NoAnswerError";
  }
}

class TimeUpError extends Error {
  constructor(message) {
    super(message);
    this.name = "TimeUpError";
  }
}

class InvalidInputError extends Error {
  constructor(message) {
    super(message);
    this.name = "InvalidInputError";
  }
}

let examTimeOver = false; 

function submitAnswer(answer) {
  try {
    if (answer === null || answer === undefined) {
      throw new NoAnswerError("No answer selected. Please choose an option.");
    }

    if (typeof answer !== "number") {
      throw new InvalidInputError("Invalid input. Answer must be a number.");
    }

    if (examTimeOver) {
      throw new TimeUpError("Exam time is over. Submission not allowed.");
    }

    console.log(`Answer ${answer} submitted successfully.`);

  } catch (error) {
    if (error instanceof NoAnswerError) {
      console.log(error.message);
    } else if (error instanceof TimeUpError) {
      console.log(error.message);
    } else if (error instanceof InvalidInputError) {
      console.log(error.message);
    } else {
      console.log("Unexpected error:", error.message);
    }
  }
}

submitAnswer(null);   
submitAnswer("A");    
examTimeOver = true;
submitAnswer(2);      
examTimeOver = false;
submitAnswer(2);     