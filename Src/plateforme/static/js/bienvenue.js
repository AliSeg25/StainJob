
/* les different type d'inscription */

document.addEventListener("DOMContentLoaded", function() {
  var interimaireOption = document.getElementById("interimaire-option");
  var employeurOption = document.getElementById("employeur-option");
      
  interimaireOption.style.display = "none";
  employeurOption.style.display = "none";

document.getElementById("inscription-dropdown").addEventListener("mouseover", function() {
  interimaireOption.style.display = "block";
  employeurOption.style.display = "block";
});

document.getElementById("inscription-dropdown").addEventListener("mouseout", function() {
  interimaireOption.style.display = "none";
  employeurOption.style.display = "none";
});

});

/* -------------------------------------------------------------------- */
window.addEventListener("load", function() {
  const loader = document.getElementById("loader");
  
  setTimeout(function() {
    loader.style.display = "none";
    document.body.classList.add("loaded");
  }, 2000); // 2000ms = 2s de pause
});