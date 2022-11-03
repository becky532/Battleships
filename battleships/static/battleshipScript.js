let dropzone = document.getElementById("dropzone");
let cursor = document.getElementById("cursor");
let enemyZone = document.getElementById("enemyZone");
const gridSquareSize = 57;
const gridSquareAmount = 7;
let boatSelected = {};
boatSelected.orientation = "horizontal";
let player1Ready = false;
let player2Ready = false;


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
    event.preventDefault(); //allows object to drop
});

dropzone.addEventListener("drop", (event)=> {
    console.log("DROPPED");
    isValid = dropValid();
    console.log(isValid);
    if (isValid){
        console.log("is valid");
    }
    else{
        console.log("is not valid");
    }
});

//async function dropValid(){
//    const response = await fetch("/validDrop/" + boatSelected.gridCoord);
//    let isValid = await response.json();
//    return isValid;
//}

async function dropValid(){
    boat = [boatSelected.gridCoord, boatSelected.shipName]
    socket.emit('shipCheck', boat)
    isValid = true
    return isValid;
}