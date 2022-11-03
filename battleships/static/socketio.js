var socket = io.connect('http://127.0.0.1:5555');

socket.on('connect', function(){
console.log('User connected!');
});

socket.on('shipCheck', validPlacement =>{
    console.log(validPlacement);
});
