let dropzone = document.getElementById("dropzone");
let cursor = document.getElementById("cursor");
let enemyZone = document.getElementById("enemyZone");
const gridSquareSize = 57;
const gridSquareAmount = 7;
let boatSelected = [];
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
      dragged = event.target;
      // make it half transparent
      event.target.classList.add("dragging");
    });

    element.addEventListener("dragend", (event) => {
      // reset the transparency
      event.target.classList.remove("dragging");
    });

});