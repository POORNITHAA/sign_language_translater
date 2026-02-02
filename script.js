const textInput = document.getElementById("text");
const charCount = document.getElementById("charCount");
const loading = document.getElementById("loading");

textInput.addEventListener("input", () => {
    charCount.innerText = `${textInput.value.length} characters`;
});

function copyText() {
    navigator.clipboard.writeText(
        document.getElementById("translatedText").innerText
    );
    alert("Copied!");
}

function startSpeech() {
    if (!("webkitSpeechRecognition" in window)) {
        alert("Use Google Chrome for speech recognition");
        return;
    }

    const recognition = new webkitSpeechRecognition();
    recognition.lang = "en-IN";

    recognition.onresult = (event) => {
        textInput.value = event.results[0][0].transcript;
        charCount.innerText = `${textInput.value.length} characters`;
    };

    recognition.start();
}

