const spawner = require('child_process').spawn;

const areaPerRouteUser=0.9;
const populationPerRouteUser=0.2;
const electrifiedUser=0.7;

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