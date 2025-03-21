let startTime;
let sentence = document.getElementById("sentence").innerText;
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
            Time Taken: ${data.timeTaken} sec<br>
            Words Per Minute: ${data.wpm} WPM<br>
            Accuracy: ${data.accuracy}%
        `;
    });
});
