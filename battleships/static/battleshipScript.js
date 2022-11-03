let dropzone = document.getElementById("dropzone");
let cursor = document.getElementById("cursor");
let enemyZone = document.getElementById("enemyZone");
const gridSquareSize = 57;
const gridSquareAmount = 7;
let boatSelected = {};
boatSelected.orientation = "horizontal";
let player1Ready = false;
let player2Ready = false;
enemyZone.addEventListener('mouseover',()=> {
    cursor.removeAttribute("style","opacity: 0");
})
enemyZone.addEventListener('mouseleave', ()=> {
    cursor.setAttribute("style","opacity: 0");
})

enemyZone.addEventListener('mousemove', event => {
  cursor.setAttribute("style", "top: "+(event.pageY - 10)+"px; left: "+(event.pageX - 10)+"px;")
})


let boatArray = Array.from(document.getElementsByClassName("boat"));
boatArray.forEach((element) => {
    // add event listener based on the data type the ships are coming in as
    // be able to click on grid to try and call a function
    // drag and drop ships
    element.addEventListener("drag", (event) => {
      console.log("dragging");
    });

    element.addEventListener("dragstart", (event) => {
      // store a ref. on the dragged elem
      boatSelected.html = event.target;
      boatSelected.shipName = event.target.id;
      console.log(boatSelected.shipName);
      event.target.classList.add("dragging");
      boatSelected.pickPoint = [event.offsetX, event.offsetY];

    });

//    element.addEventListener("dragover", (event) => {
//      // reset the transparency
//      event.target.classList.remove("dragging");
//      console.log("dragging over box");
//    });

    element.addEventListener("dragend", (event) => {
      // reset the transparency
      event.target.classList.remove("dragging");
      console.log("THE INPUT COORDS ARE " + boatSelected.gridCoord);
    });

});

dropzone.addEventListener("dragover", (event)=> {
    let xCoord = Math.round((event.offsetX-boatSelected.pickPoint[0])/gridSquareSize);
    console.log("Xcoord = " + xCoord);
    let yCoord = Math.round((event.offsetY-boatSelected.pickPoint[1])/gridSquareSize);
    console.log("Ycoord = " + yCoord);
    boatSelected.gridCoord = [xCoord, yCoord];
    boatSelected.position = [xCoord * gridSquareSize, yCoord * gridSquareSize]
    event.preventDefault(); //allows object to drop
});

dropzone.addEventListener("drop", (event)=> {
    console.log("DROPPED");
    dropValid()
});

//async function dropValid(){
//    const response = await fetch("/validDrop/" + boatSelected.gridCoord);
//    let isValid = await response.json();
//    return isValid;
//}

function dropValid(){
    boat = [boatSelected.gridCoord, boatSelected.shipName];
    socket.emit('shipCheck', boat);
}

function placeShip(){
    dropzone.appendChild(boatSelected.html)
    boatSelected.html.style.transform = `translate(${boatSelected.position[0]}px,${boatSelected.position[1]}px)`
    boatSelected.html.style.position = "absolute"
}

$('#all-ready').on('click', function() {
    socket.emit('readyCheck')
})

enemyZone.addEventListener("click", (event) => {
    if (player1Ready && player2Ready) {
        let xCoord = Math.round(event.offsetX/gridSquareSize);
        console.log("Xcoord = " + xCoord);
        let yCoord = Math.round(event.offsetY/gridSquareSize);
        console.log("Ycoord = " + yCoord);
        let coord = [xCoord, yCoord]
        socket.emit('attack', coord)
    }
});

function showAttackResult(attackResult, coord){
    player = document.getElementById('enemyZone');
    console.log('showAttackResult');
    console.log(coord);
    console.log(player);
    if (attackResult) {
        decorateHit(coord, player);
    }
    else {
        decorateMiss(coord, player);
    }
}

function showEnemyAttack(attackResult, coord){
    player = document.getElementById('dropzone');
    console.log('showEnemyAttack');
    console.log(coord);
    console.log(player);
    if (attackResult) {
        decorateHit(coord, player);
    }
    else {
        decorateMiss(coord, player);
    }
}

function decorateHit(coord, player){
  player.innerHTML += `
  <div class="fire" style="transform: translate(${(coord[0]*57)+11.4}px, ${(coord[1]*57)-40}px)">
  <div class="hole3"></div>
  <div class="hole2"></div>
  <div class="hole1"></div>
  <div class="flame1"></div>
  <div class="flame2"></div>
  <div class="flame3"></div>
  <div class="flame4"></div>
  <div class="flame5"></div>
</div>`
}

function decorateMiss(coord){
  player.innerHTML += `
  <div class="w" style="transform: translate(${coord[0]*57}px, ${coord[1]*57}px)">
  <div class="water1"></div>
  <div class="water2"></div>
  <div class="water3"></div>
  <div class="water4"></div>
  <div class="water5"></div>
  </div>
  `
}