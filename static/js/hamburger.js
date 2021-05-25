// Opening the hamburger menu.
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-left");

hamburger.addEventListener("click", mobileMenu);

function mobileMenu() {
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
}
// Close hamburger menu when an item is clicked in it.
const navLink = document.querySelectorAll(".nav-left");
navLink.forEach(n => n.addEventListener("click", closeMenu));

function closeMenu() {
    hamburger.classList.remove("active");
    navMenu.classList.remove("active");
}