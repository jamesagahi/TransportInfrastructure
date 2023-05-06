
slider = document.querySelectorAll("input")[0];
slider.oninput = update;

slider1 = document.querySelectorAll("input")[1];
slider1.oninput = update1;

slider2 = document.querySelectorAll("input")[2];
slider2.oninput = update2;

function update() {
    progressBar = document.querySelector("progress");
    progressBar.value = slider.value;
    sliderValue = document.querySelector(".sliderValue");
    sliderValue.innerHTML = slider.value;
    sendInfo();
}

function update1() {
    progressBar1 = document.querySelectorAll("progress")[1];
    progressBar1.value = slider1.value;
    sliderValue1 = document.querySelectorAll(".sliderValue")[1];
    sliderValue1.innerHTML = slider1.value;
    sendInfo();
}
function update2() {
    progressBar = document.querySelectorAll("progress")[2];
    progressBar.value = slider2.value;
    sliderValue = document.querySelectorAll(".sliderValue")[2];
    sliderValue.innerHTML = slider2.value;
    sendInfo();
}

function sendInfo() {
    console.log("("+slider.value + ", " +
                slider1.value + ", " +
                slider2.value + ")");
}