
var mode_task_on = 0;
var mode_comment_on = 0;
var editing_comment_id = 0;

//on and off edit mode
function edit_task_mode_click (task_id){

    if (mode_task_on == 0){

        var button= document.getElementById("edit_mode_task").className = "fas fa-md fa-fw fa-edit text-gray-100";
        var div_button = document.getElementsByClassName("right_icon_edit")[0];
        div_button.style.backgroundColor = '#3A3B45';
        mode_task_on =1;
        approve_appear("Edit task mode is ON");
        var description = document.getElementById("task_desc");
        description.setAttribute("contenteditable", true);
        var name = document.getElementById("task_name");
        name.setAttribute("contenteditable", true);
        var task_date = document.getElementById("task_date");
        task_date.setAttribute("contenteditable", true);

    }
    else {
        var button= document.getElementById("edit_mode_task").className = "fas fa-md fa-fw fa-edit text-gray-900";
        var div_button = document.getElementsByClassName("right_icon_edit")[0];
        div_button.style.backgroundColor = '#f8f9fc';
        mode_task_on =0;
        var description = document.getElementById("task_desc");
        description.setAttribute("contenteditable", false);
        var name = document.getElementById("task_name");
        name.setAttribute("contenteditable", false);
        var task_date = document.getElementById("task_date");
        task_date.setAttribute("contenteditable", false);

        post_update_task(name.innerHTML, description.innerHTML, task_date.innerHTML, task_id);
    }

}

edit_comment_mode_click (task_id, comment_id){

    if (mode_comment_on == 0 && editing_comment_id == 0){

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
function post_update_task ( name, description, finish_date, task_id ){

    alert (task_id);
    $.ajax({
        url: "/task/update/"+task_id+"/",
        method:"POST",
        data: {
          'name': name,
          'description':description,
          'finish_date':finish_date
        },
        dataType: 'json',
        success: function (data) {
          approve_appear("Changes saved ");
        }
      });



}