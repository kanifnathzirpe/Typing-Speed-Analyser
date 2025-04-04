let startTime;
let sentence = document.getElementById("sentence").textContent;
let typingArea = document.getElementById("typingArea");
let submitBtn = document.getElementById("submitBtn");
let result = document.getElementById("result");


typingArea.addEventListener("keydown", () => {
    if (!startTime) startTime = Date.now();
});

submitBtn.addEventListener("click", () => {
    let typedText = typingArea.value;
    let endTime = Date.now();
    
    fetch("/calculate-speed", {
        method: "POST",
        body: JSON.stringify({
            sentence: sentence,
            typedText: typedText,
            startTime: startTime / 1000  
        }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        result.innerHTML = `
            <b>Analysis: </b> <br><br>
            Time Taken: ${data.timeTaken} sec<br>
            Words Per Minute: ${data.wpm} WPM<br>
            Accuracy: ${data.accuracy}%
        `;
    });
});


let timer = document.querySelector(".timer");
let chkbtn = document.querySelector("#submitBtn");

function timerCountdown() {
    
    let timeCount = 30;
    const countdown = setInterval(async () => {
        if (timeCount <= 0) {
            clearInterval(countdown);
            timer.textContent = "Time's Up!";
            await submitBtn.click();
            await typingArea.blur();

        } else {
            timeCount--;
            timer.textContent = timeCount;
        }
        
    }, 1000);    

    
    chkbtn.addEventListener("click", () => {
        timer.textContent = timeCount;
        clearInterval(countdown);
        result.scrollIntoView({ behavior: "smooth" });
    });        
}