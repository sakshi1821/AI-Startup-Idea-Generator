
// ===============================
// Theme Toggle
// ===============================

const themeBtn = document.getElementById("themeBtn");

if (localStorage.getItem("theme") === "light") {
    document.body.classList.add("light-mode");
    themeBtn.innerHTML = "🌙 Dark Mode";
}

themeBtn.addEventListener("click", () => {

    document.body.classList.toggle("light-mode");

    if (document.body.classList.contains("light-mode")) {
        themeBtn.innerHTML = "🌙 Dark Mode";
        localStorage.setItem("theme", "light");
    } else {
        themeBtn.innerHTML = "☀️ Light Mode";
        localStorage.setItem("theme", "dark");
    }

});

// ===============================
// Animated Success Bar
// ===============================

const progressBar = document.querySelector(".progress-bar");

if (progressBar) {

    const target = parseInt(progressBar.dataset.success);

    let width = 0;

    progressBar.style.width = "0%";
    progressBar.innerHTML = "0%";

    const animation = setInterval(() => {

        if (width >= target) {
            clearInterval(animation);
        } else {
            width++;
            progressBar.style.width = width + "%";
            progressBar.innerHTML = width + "%";
        }

    }, 15);

}

