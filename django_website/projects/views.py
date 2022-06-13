from django.shortcuts import render

from projects.models import Project


def project_index(request):
    projects = Project.objects.all()

    for p in projects:
        path = p.image
        static_path = path.split("/")[-2] + "/" + path.split("/")[-1]
        p.image = static_path
        p.description = p.description[:min(len(p.description),50)]+"..."

    context = {
        'projects': projects
    }

    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    
    path = project.image
    static_path = path.split("/")[-2] + "/" + path.split("/")[-1]
    project.image = static_path

    project.title = project.title.upper()

    context = {
        'project': project
    }

    return render(request, 'project_detail.html', context)