function quizGame() {
    //   private variable
    let score = 0;

    return {
        correct: function () {
        score++;
        console.log(`Score: ${score}`);
        },
        wrong: function () {
        score--;
        console.log(`Score: ${score}`);
        }
    };
}

const player1 = quizGame();
player1.correct(); 
player1.correct();
player1.wrong();