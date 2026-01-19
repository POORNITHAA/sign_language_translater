// Change button text while submitting (simple feedback)
const form = document.querySelector("form");
const button = form.querySelector("button");

form.addEventListener("submit", () => {
    button.innerText = "Translating...";
    button.disabled = true;
});