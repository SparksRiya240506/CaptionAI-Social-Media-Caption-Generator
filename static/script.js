const darkBtn = document.getElementById("dark-btn");

if (darkBtn) {
    darkBtn.addEventListener("click", () => {
        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {
            darkBtn.innerText = "☀️ Light Mode";
        } else {
            darkBtn.innerText = "🌙 Dark Mode";
        }
    });
}

// Copy Function
function copyText(id) {
    const text = document.getElementById(id).innerText;
    navigator.clipboard.writeText(text);
    alert("Copied to clipboard!");
}

// Loading Spinner
const form = document.getElementById("captionForm");

if (form) {
    form.addEventListener("submit", function () {
        const loader = document.getElementById("loader");

        if (loader) {
            loader.style.display = "block";
        }
    });
}