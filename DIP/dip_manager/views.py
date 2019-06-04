from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from dip_manager.models import Project, User, Task, Comment, Pic_Task, Pic_comm, Suggestion
import pandas as pd
from dip_manager.forms import ImageUploadForm, ImageUploadForm_comm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import pytz
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.http import JsonResponse



@login_required
def dependencies (request):
    return render(request, 'dependencies.html', {})


@login_required
def generate_report_users(request):

    users = []
    indexes =[]
    for i in User.objects.all():
        users.append([i.username, i.first_name, i.last_name, i.password])
        indexes.append (len(users))
    users_df = pd.DataFrame(users, index = indexes,columns = ['username', 'first name', 'last name', 'password'])
    users_df.to_excel("users.xlsx", sheet_name = 'Users')
    return render(request, '404.html', {})


@login_required
@csrf_exempt
def report_suggest(request):
    if request.method == 'POST':

        print ("I do work")
        if (request.POST.get('creator')== "all"):
            suggestions = Suggestion.objects.filter(created_at__range=(request.POST.get('date_start'), request.POST.get('date_end')))
        else:
            suggestions = Suggestion.objects.filter(
                date_post__range=(request.POST.get('date_start'), request.POST.get('date_end')),
                creator = get_object_or_404(User, pk=request.POST.get('creator')))

        suggs = []
        indexes=[]

        for i in suggestions:
            suggs.append([i.creator.username, i.text, i.date_post])
            indexes.append(len(suggs))
        suggs_df = pd.DataFrame(suggs, index=indexes, columns=['username', 'text', 'date posted'])
        suggs_df.to_excel("suggestions_report.xlsx", sheet_name='Suggestions')

        return JsonResponse({})




@login_required
def task_pic (request):


    task = get_object_or_404(Task, pk=request.POST.get('task'))

    print (task.task_name, task.creator)

    if request.method == "POST":

        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():

            task_pic_new = Pic_Task(task=get_object_or_404(Task, pk=request.POST.get('task')))
            task_pic_new.picture = form.cleaned_data['image']
            task_pic_new.save()



    return HttpResponseRedirect(reverse('task_detail', kwargs = {'id': task.id}))


@login_required
def account (request):

    return render(request, 'account_settings.html', {"user": request.user})


@login_required
def tasks(request):

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


@login_required
def task_detail(request, id):

    task = get_object_or_404(Task, pk=id)


    if request.method == "POST":

        form = ImageUploadForm_comm(request.POST, request.FILES)


        comment = Comment.objects.create_comment(request.POST.get('text'),request.user,
                                       get_object_or_404(Task, pk=request.POST.get('task')))

        if form.is_valid():

            comm_pic_new = Pic_comm(comment=comment, task=task)

            comm_pic_new.picture = form.cleaned_data['image_comm']

            comm_pic_new.save()



    print (Pic_comm.objects.all().filter(task=task))

    return render(request, 'task_detail.html', {'task': task,
                                                'comments': Comment.objects.all().filter(task=task).order_by('-date_post'),
                                                'pics_task': Pic_Task.objects.all().filter(task=task),
                                                'pics_comm': Pic_comm.objects.all().filter(task=task)
                               })
@login_required
def task_delete(request, id):

    task = get_object_or_404(Task, pk=id).delete()

    return HttpResponseRedirect(reverse('home'))


@login_required
@csrf_exempt
def task_update(request, id):
    if (request.POST.get('finish_date')[-5:] == " a.m."):
        date_finish = request.POST.get('finish_date')[:-5]+"AM"
    else:
        date_finish = request.POST.get('finish_date')[:-5] + "PM"
    Task.objects.filter(id=id).update(task_name = request.POST.get('name'),
                                                 description =request.POST.get('description'),
                                                 date_end = datetime.strptime(date_finish[8:],'%b %d, %Y, %I:%M%p'),
                                                 date_update = timezone.now(), updated = 1)

    return JsonResponse({'status': 'success'})


@login_required
def comment_delete(request, task_id, comment_id):

    comment = get_object_or_404(Comment, pk=comment_id).delete()

    return HttpResponseRedirect(reverse('task_detail', kwargs={'id': task_id}))



@login_required
@csrf_exempt
def comment_update(request, task_id, comment_id):

    Comment.objects.filter(id = comment_id).update(text = request.POST.get('text'),
                                                   date_update = timezone.now(),
                                                   updated=1 )

    return JsonResponse({'status': 'success'})


@login_required
def projects(request):

    if request.method == "POST":

        Project.objects.create_project(request.POST.get('project_name'), request.POST.get('description'))


    return render(request, 'projects.html', {"projects": Project.objects.all()})


@login_required
def proj_detail(request, id):

    project = get_object_or_404(Project, pk=id)

    return render(request, 'project_detail.html', {'project': project})


@login_required
def proj_delete(request, id):

    project = get_object_or_404(Project, pk=id).delete()

    return HttpResponseRedirect(reverse('projects'))


@login_required
@csrf_exempt
def project_update(request, id):

    Project.objects.filter(id = id).update(project_name = request.POST.get('project_name'),
                                        description=request.POST.get('description') )

    return JsonResponse({'status': 'success'})




@login_required
def users(request):

    if request.method == "POST":

        user = User.objects.create_user( username = request.POST.get('username'), first_name=request.POST.get('first_name'),
                          last_name=request.POST.get('last_name'), user_position=request.POST.get('user_position'),
                          user_type= request.POST.get('user_type'), password=request.POST.get('password') )

    return render(request, 'users.html', {"users": User.objects.all()})



@login_required
def user_detail(request, id):

    user = get_object_or_404(User, pk=id)

    return render(request, 'user_detail.html', {'user': user})


@login_required
def user_delete(request, id):

    user = get_object_or_404(User, pk=id).delete()

    return HttpResponseRedirect(reverse('users'))


@login_required
@csrf_exempt
def user_update(request, id):

    User.objects.filter(id = id).update(first_name = request.POST.get('first_name'),
                                        last_name=request.POST.get('last_name'),
                                        username=request.POST.get('username'),
                                        user_position = request.POST.get('position') )

    return JsonResponse({'status': 'success'})



@login_required
@csrf_exempt
def suggest(request):

    bar_approve=0
    if request.method == 'POST':

        suggestion = Suggestion (creator =  request.user, date_post = timezone.now(),
                                 text = request.POST.get('text_sugg'))
        suggestion.save()
        suggestion.followers.add(request.user)
        suggestion.save()
        print (suggestion.followers)
        bar_approve = 1

    return render(request, 'suggest.html', {"bar": bar_approve})



@login_required
def suggestions(request):

    return render(request, 'suggestions.html', {"suggestions": Suggestion.objects.all()})


