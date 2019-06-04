//changes approval bar downside
function approve_appear(text) {

  var approve = document.getElementById("snackbar");

  var icon = document.createElement("i");

  icon.className = "fas fa-check-circle text-success";

  approve.innerHTML = text;

  approve.className = "show";

  approve.appendChild(icon);

  setTimeout(function(){ approve.className = approve.className.replace("show", ""); }, 3000);

}


