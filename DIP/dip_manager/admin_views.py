from django.shortcuts import render


def project(request):
    return render(request, 'projects.html', {})



def changes(request):
    return render(request, 'admin_changes.html', {})