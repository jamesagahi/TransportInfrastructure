const spawner = require('child_process').spawn;

console.log("Running")

process = spawner('py', ["./test.py"]);
//console.log(process);

process.stdout.on('data', (data) => {
    console.log(data)
})

process.stderr.on('data', data => {
    console.log('stderr: ' + data.toString())
})

process.on('close', code => {
    console.log("CLOSE")


})

console.log("END")