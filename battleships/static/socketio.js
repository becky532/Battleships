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
    document.getElementById("clear-board").classList.add('invisible');
    stopBoatsDragging();
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

socket.on('gameVictory', ()=> {
    alert('YOU WON! WOOO!');
    setTimeout(function(){ window.location.href= '/victory';}, 3000);
});

socket.on('gameDefeat', ()=> {
    alert('Better luck next time. Loser.');
    setTimeout(function(){ window.location.href= '/defeat';}, 3000);
});

socket.on('rotate', (newOrientation)=> {
    rotate(newOrientation);
});