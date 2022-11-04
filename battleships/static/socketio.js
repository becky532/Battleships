var socket = io.connect('http://127.0.0.1:5555');

socket.on('connect', function(){
console.log('User connected!');
});

socket.on('shipCheck', validPlacement => {
    if (validPlacement) {
        placeShip()
    }
});

socket.on('personalReady', (playerNum) => {
    console.log(playerNum);
    if (playerNum == 0){
        player1Ready = true;
    }
    else if (playerNum == 1){
        player2Ready = true;
    }
    document.getElementById('all-ready').classList.add("invisible");
    stopBoatsDragging();
    // ADD CODE TO STOP SHIPS BEING DRAGGED, HIDE BOAT TEXT
});

socket.on('enemyReady', (playerNum) => {
    console.log(playerNum);
    if (playerNum == 0){
        player1Ready = true;
    }
    else if (playerNum == 1){
        player2Ready = true;
    }
});

socket.on('attackResult', (attackResult, coord) => {
    showAttackResult(attackResult, coord);
});

socket.on('defenceResult', (attackResult, coord) => {
    showEnemyAttack(attackResult, coord);
});