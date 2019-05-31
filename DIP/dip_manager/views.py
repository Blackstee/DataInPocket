from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from dip_manager.models import Project, User, Task



def account (request):

    if request.user.is_authenticated:

        return render(request, 'account_settings.html', {"user": request.user})


def tasks(request):

    if request.user.is_authenticated:


        if request.method == "POST":

            task = Task(task_name=request.POST.get('task_name'), description=request.POST.get('description'),
                                     date_start = request.POST.get('date_start'), date_end = request.POST.get('date_end'),
                                     date_update = request.POST.get('date_start'), updated = 0,
                                     creator = request.user, doer = get_object_or_404(User, pk=request.POST.get('doer')),
                                     project = get_object_or_404(Project, pk=request.POST.get('project')))
            task.save()
            task.followers.add(request.user, get_object_or_404(User, pk=request.POST.get('doer')))
            task.save()


        return render(request, 'tasks.html', {"projects": Project.objects.all(), "users": User.objects.all(),
                                              "tasks": Task.objects.all()})

def task_detail(request, id):

    task = get_object_or_404(Task, pk=id)

    return render(request, 'task_detail.html', {'task': task})


def task_delete(request, id):

    task = get_object_or_404(Task, pk=id).delete()

    return HttpResponseRedirect(reverse('tasks'))




def projects(request):

    if request.user.is_authenticated:

        if request.method == "POST":

            Project.objects.create_project(request.POST.get('project_name'), request.POST.get('description'))


        return render(request, 'projects.html', {"projects": Project.objects.all()})



def proj_detail(request, id):

    project = get_object_or_404(Project, pk=id)

    return render(request, 'project_detail.html', {'project': project})


def proj_delete(request, id):

    project = get_object_or_404(Project, pk=id).delete()

    return HttpResponseRedirect(reverse('projects'))




def users(request):

    if request.user.is_authenticated:

        if request.method == "POST":

            user = User.objects.create_user( username = request.POST.get('username'), first_name=request.POST.get('first_name'),
                          last_name=request.POST.get('last_name'), user_position=request.POST.get('user_position'),
                          user_type= request.POST.get('user_type'), password=request.POST.get('password') )
            #user.save()

            #User.objects.create_user(request.POST.get('username'), request.POST.get('first_name'),
            #                         request.POST.get('last_name'), request.POST.get('user_position'),
             #                        request.POST.get('user_type'), request.POST.get('password'))

        return render(request, 'users.html', {"users": User.objects.all()})



def user_detail(request, id):

    user = get_object_or_404(User, pk=id)

    return render(request, 'user_detail.html', {'user': user})

def user_delete(request, id):

    user = get_object_or_404(User, pk=id).delete()

    return HttpResponseRedirect(reverse('users'))
