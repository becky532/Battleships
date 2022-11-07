$('#all-ready').on('click', function() {
    socket.emit('readyCheck');
})

enemyZone.addEventListener("click", (event) => {
    if (player1Ready && player2Ready) {
        let xCoord = Math.floor(event.offsetX/gridSquareSize);
        console.log("Xcoord = " + xCoord);
        let yCoord = Math.floor(event.offsetY/gridSquareSize);
        console.log("Ycoord = " + yCoord);
        let coord = [xCoord, yCoord]
        socket.emit('attack', coord)
    }
});