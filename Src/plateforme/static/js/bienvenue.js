
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
