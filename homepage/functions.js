/*
var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 3000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}
*/


function myFunction() {
  const images = document.querySelectorAll("img"); // Select all images
  let loadedImages = 0;

  images.forEach((img) => {
      // Add an event listener for each image
      img.addEventListener("load", imageLoaded);
      img.addEventListener("error", imageLoaded); // Handle errors as well
  });

  function imageLoaded() {
      loadedImages++;
      // Check if all images are loaded
      if (loadedImages === images.length) {
          showPage();
      }
  }
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}
