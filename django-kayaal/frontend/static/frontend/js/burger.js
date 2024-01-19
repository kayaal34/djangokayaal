let burger = document.querySelector(".header__burger");
let menu = document.querySelector(".header__navigation-container");
let links = document.querySelectorAll(".navigation__item");
let closeBurger =  document.querySelector(".navigation__burger");


menu.style.display = "block"

burger.addEventListener('click', getBurgerMenu);
closeBurger.addEventListener("click", closeBurgerMenu);
links.forEach( (link) => {
    link.addEventListener("click", closeBurgerMenu)
});


function getBurgerMenu() {
    menu.classList.add("header__navigation-container--active");
    document.body.classList.add("stop-scroll");
}

function closeBurgerMenu(event) {
    menu.classList.remove("header__navigation-container--active");
    document.body.classList.remove("stop-scroll");
}