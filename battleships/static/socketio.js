window.onload = function() {
    var socket = io.connect('http://127.0.0.1:5555');
    socket.on('connect', function(){
    socket.send('User connected!');
    });
}
