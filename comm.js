const jsdom=require("jsdom");
const{JSDOM}=jsdom
global.document=new JSDOM("ui.html").window.document;
const inputElement = dom.window.document.getElementId('myInput')



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

const spawner = require('child_process').spawn;

const areaPerRouteUser=slider.value/100.0;
const populationPerRouteUser=slider1.value/100.0;
const electrifiedUser=slider2.value/100.0;

const data_to_pass_in=[areaPerRouteUser,populationPerRouteUser, electrifiedUser]


console.log('Data sent to python script:',data_to_pass_in);

python_process = spawner('py', ['./backend.py', data_to_pass_in[0], data_to_pass_in[1], data_to_pass_in[2]]);

console.log('hi')
//console.log('e')

python_process.stdout.on('data', (data) => {
    console.log('Data received from python script:', data.toString());
});

python_process.stderr.on('data', (data) => {
    console.log('stderr:', data.toString());
});

//console.log('ee')

//////


var http = require('http');
var fs = require('fs');

http.createServer((req, res) => {
    console.log(req.url)
    if (req.url === "/") {
        fs.readFile('ui.html', (err, html) => {
            if (err) {
                throw err;
            }
            res.setHeader('Content-type', 'text/html');
            res.write(html);
            res.statusCode = 200;
            res.end();
        });
    }
    else if (req.url == '/style.css') {
        res.setHeader('Content-type', 'text/css');
        res.write(fs.readFileSync('style.css'));
        res.end();
    } else {
        res.write("invalid request")
        res.end();
    }
}).listen(3000);

console.log('server running @ 3000');

////
