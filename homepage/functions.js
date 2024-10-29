
var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 3000);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myDiv").style.display = "block";
}


 window.onload = function() {
  document.getElementById("loader").style.display = "none"; // Hide loader
  document.getElementById("myDiv").style.display = "block"; // Show main content
};
