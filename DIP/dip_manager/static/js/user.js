
function appear_button_save(user_id){

    if($('#user_change').length <= 0){
        var br_ = document.createElement("br");
        var icon = document.createElement("i");

        icon.className = "my_edit_user fas fa-lg fa-paper-plane text-warning";

        icon.id = "user_change";
        icon.onclick = function(){
        post_update_user(user_id);
        }


        var user = document.getElementById("user_ticket");

        user.appendChild (br_);
        user.appendChild (icon);


    }

}




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


//sends updates of task to server
function post_update_user ( user_id ){

    var first_name = document.getElementById("first_name").innerHTML;
    var last_name = document.getElementById("last_name").innerHTML;
    var username = document.getElementById("username").innerHTML;
    var position = document.getElementById("position").innerHTML;
    //var type = document.getElementById("type").innerHTML;

    $.ajax({
        url: "/user/update/"+user_id+"/",
        method:"POST",
        data: {
          'first_name': first_name,
          'last_name': last_name,
          'username':username,
          'position':position
        },
        dataType: 'json',
        success: function (data) {
          approve_appear("Changes for user saved ");
        }
      });



}