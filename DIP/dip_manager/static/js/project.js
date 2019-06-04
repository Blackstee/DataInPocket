
function appear_button_save(project_id){

    if($('#project_change').length <= 0){
        var br_ = document.createElement("br");
        var icon = document.createElement("i");

        icon.className = "my_edit_user fas fa-lg fa-paper-plane text-warning";

        icon.id = "project_change";
        icon.onclick = function(){
        post_update_project(project_id);
        }


        var user = document.getElementById("project_ticket");

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
function post_update_project ( project_id ){

    var project_name = document.getElementById("project_name").innerHTML;
    var description = document.getElementById("description").innerHTML;

    $.ajax({
        url: "/project/update/"+project_id+"/",
        method:"POST",
        data: {
          'project_name': project_name,
          'description': description
        },
        dataType: 'json',
        success: function (data) {
          approve_appear("Changes for project saved ");
        }
      });



}