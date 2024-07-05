from django.shortcuts import render, get_object_or_404
from .models import Project, Tag, Experience, Education

# Create your views here.

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def experience_view(request):
    experiences = Experience.objects.all()
    education_list = Education.objects.all()
    return render(request, 'experience.html', {'experiences': experiences, 'education_list': education_list})

def projectlist(request):
    projects = Project.objects.prefetch_related('images').all()
    tags = Tag.objects.all()
    return render(request, 'projectlist.html', {'projects': projects, 'tags': tags})

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {'project': project})

