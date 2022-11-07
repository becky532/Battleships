let dropzone = document.getElementById("dropzone");
let cursor = document.getElementById("cursor");
let enemyZone = document.getElementById("enemyZone");
const gridSquareSize = 57;
const gridSquareAmount = 7;
let boatSelected = {};
let player1Ready = false;
let player2Ready = false;
enemyZone.addEventListener('mouseover', ()=> {
    cursor.removeAttribute("style","opacity: 0");
})
enemyZone.addEventListener('mouseleave', ()=> {
    cursor.setAttribute("style","opacity: 0");
})

enemyZone.addEventListener('mousemove', event => {
  cursor.setAttribute("style", "top: "+(event.pageY - 10)+"px; left: "+(event.pageX - 10)+"px;")
})

function initialiseBoats(){
    let boatArray = Array.from(document.getElementsByClassName("boat"));
    boatArray.forEach((element) => {
        // add event listener based on the data type the ships are coming in as
        // be able to click on grid to try and call a function
        // drag and drop ships
        element.addEventListener("drag", (event) => {
        });

        element.addEventListener("dragstart", (event) => {
          // store a ref. on the dragged elem
          boatSelected.html = event.target;
          boatSelected.shipName = event.target.id;
          console.log(boatSelected.shipName);
          event.target.classList.add("dragging");
          boatSelected.pickPoint = [event.offsetX, event.offsetY];
          socket.emit('removeBoatIfOnBoard', boatSelected.shipName)
        });
        element.addEventListener("dragend", (event) => {
          // reset the transparency
          event.target.classList.remove("dragging");
          console.log("THE INPUT COORDS ARE " + boatSelected.gridCoord);
        });

    });
}
initialiseBoats();

dropzone.addEventListener("dragover", (event)=> {
    let xCoord = Math.round((event.offsetX-boatSelected.pickPoint[0])/gridSquareSize);
    let yCoord = Math.round((event.offsetY-boatSelected.pickPoint[1])/gridSquareSize);
    boatSelected.gridCoord = [xCoord, yCoord];
    boatSelected.position = [xCoord * gridSquareSize, yCoord * gridSquareSize];
    event.preventDefault(); //allows object to drop
});

dropzone.addEventListener("drop", (event)=> {
    console.log("DROPPED");
    dropValid();
});


function dropValid(){
    boat = [boatSelected.gridCoord, boatSelected.shipName];
    socket.emit('shipCheck', boat);
}

function placeShip(){
    dropzone.appendChild(boatSelected.html);
    boatSelected.html.style.transform = `translate(${boatSelected.position[0]}px,${boatSelected.position[1]}px)`;
    boatSelected.html.style.position = "absolute";
    console.log('ERROR CHECK');
    console.log(boatSelected.html.getAttribute('addedRotation'));
    if (boatSelected.html.getAttribute('addedRotation') !== 'true') {
        addRotation();
        boatSelected.html.setAttribute('addedRotation','true');
    }
}

function addRotation(){
    boatSelected.html.addEventListener('click', (event)=> {
        console.log('rotating');
        boatSelected.shipName = event.currentTarget.id;
        boatSelected.html = document.querySelector(`#${boatSelected.shipName}`);
        boatSelected.htmlBody = document.querySelector(`#${boatSelected.shipName}-body`);
        socket.emit('rotate', boatSelected.shipName);
    });
}

function rotate(newOrientation){
    if (newOrientation == 'vertical') {
        boatSelected.htmlBody.classList.remove(`${boatSelected.shipName}`);
        boatSelected.htmlBody.classList.add(`${boatSelected.shipName}R`);
        boatSelected.html.classList.remove(`${boatSelected.shipName}-container`);
        boatSelected.html.classList.add(`${boatSelected.shipName}-containerR`);
    }
    else {
        boatSelected.htmlBody.classList.remove(`${boatSelected.shipName}R`);
        boatSelected.htmlBody.classList.add(`${boatSelected.shipName}`);
        boatSelected.html.classList.remove(`${boatSelected.shipName}-containerR`);
        boatSelected.html.classList.add(`${boatSelected.shipName}-container`);
    }
        console.log('Done rotation');
}



$('#all-ready').on('click', function() {
    socket.emit('readyCheck');
})

$('#clear-board').on('click', function() {
    socket.emit('clearBoard');
    boatsOnGrid = document.querySelectorAll("#dropzone .boat").forEach((element) => element.remove());
    resetBoats();
    initialiseBoats();
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

function showAttackResult(attackResult, coord){
    player = enemyZone;
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
    player = dropzone;
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

function stopBoatsDragging(){
    boatArray.forEach((element) => {
        element.setAttribute("draggable", false);
    });
    document.querySelector(".boats-here").classList.add('invisible');
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

function resetBoats(){
    document.getElementById('boats-menu').innerHTML = `
            <div class="boat carrier-container shadow" id="carrier" draggable="true">
                <div class="carrier" id="carrier-body">
                    <div class="carrier-part carrier-base p1color"></div>
                    <div class="carrier-part shadow">
                        <div class="carrier-part carrier-platform p1color"></div>
                        <div class="carrier-lines1"></div>
                        <div class="carrier-lines2"></div>
                        <div class="carrier-lines3"></div>
                    </div>
                </div>
            </div>
            <div class="boat battleship-container shadow" id="battleship" draggable="true">
                <div class="battleship" id="battleship-body">
                    <div class="battleship-part battleship-base p1color shadow"></div>
                    <div class="battleship-part shadow">
                        <div class=" battleship-part battleship-heliport p1color shadow"></div>
                        <div class="battleship-part shadow">
                            <div class=" battleship-part battleship-helicopter p1color"></div>
                            <div class=" battleship-part battleship-cover p1color"></div>
                            <div class=" battleship-part battleship-antena p1color"></div>
                            <div class=" battleship-part battleship-front p1color"></div>
                            <div class="battleship-part shadow">
                                <div class=" battleship-part battleship-cannon p1color"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="boat cruiser-container shadow" id="cruiser" draggable="true">
                <div class="cruiser" id="cruiser-body">
                    <div class="cruiser-part cruiser1 p1color"></div>
                    <div class="cruiser-part shadow">
                        <div class="cruiser-part cruiser2 p1color"></div>
                        <div class="cruiser-part shadow">
                            <div class="cruiser-part cruiser3 p1color"></div>
                            <div class="cruiser-part shadow">
                                <div class="cruiser-part cruiser4 p1color"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="boat submarine-container shadow" id="submarine" draggable="true">
                <div class="submarine" id="submarine-body">
                    <div class="submarine-part shadow">
                        <div class="submarine-part submarine1 p1color"></div>
                        <div class="submarine-part shadow">
                            <div class="submarine-part submarine2 p1color">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="boat destroyer-container shadow" id="destroyer" draggable="true">
                <div class="destroyer" id="destroyer-body">
                    <div class="destroyer-part shadow">
                        <div class="destroyer-part p1color destroyer1 "></div>
                        <div class="destroyer-part shadow">
                            <div class="destroyer-part p1color destroyer2"></div>
                            <div class="destroyer-part p1color destroyer3">
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    `;
}