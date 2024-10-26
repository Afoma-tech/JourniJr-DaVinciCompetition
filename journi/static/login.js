const loginBtn = document.querySelector("#login");
const registerBtn = document.querySelector("#register");
const loginForm = document.querySelector(".login-form");
const registerForm = document.querySelector(".register-form");

loginBtn.addEventListener('click', () => {
    loginBtn.style.backgroundColor = "#12a088";
    loginBtn.style.color = "#fff";
    registerBtn.style.backgroundColor = "rgba(200, 200, 200, 0.2)";
    registerBtn.style.color = "#404246";

    loginForm.style.left = "50%";
    registerForm.style.left = "-50%";

    loginForm.style.opacity = 1;
    registerForm.style.opacity = 0;

    document.querySelector(".col-1").style.borderRadius = "0 30% 20% 0";
})

registerBtn.addEventListener('click', () => {
    loginBtn.style.backgroundColor = "rgba(200, 200, 200, 0.2)";
    loginBtn.style.color = "#404246";
    registerBtn.style.backgroundColor = "#12a088";
    registerBtn.style.color = "#fff";

    loginForm.style.left = "150%";
    registerForm.style.left = "50%";

    loginForm.style.opacity = 0;
    registerForm.style.opacity = 1;

    document.querySelector(".col-1").style.borderRadius = "0 20% 30% 0";
})
