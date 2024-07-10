from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Project, Tag, Experience, Education
import random

# Create your views here.

def home(request):
    # Fetch all projects and prefetch related images
    projects = list(Project.objects.prefetch_related('images').all())
    # Shuffle the list of projects randomly
    random.shuffle(projects)
    # Fetch all tags (if needed)
    tags = Tag.objects.all()
    if request.method == "POST":
        message_name = request.POST.get('message-name')
        message_email = request.POST.get('message-email')
        message = request.POST.get('message')

        if message_name and message_email and message:
            try:
                send_mail(
                    subject=message_name,
                    message=message,
                    from_email=message_email,
                    recipient_list=['olutayoogunlade2022@gmail.com'],
                )
                return render(request, "home.html", {
                    "message_name": message_name, 
                    "message_email": message_email, 
                    "message": message,
                    "success": True
                })
            except BadHeaderError:
                return HttpResponseBadRequest('Invalid header found.')
        else:
            return HttpResponseBadRequest('Ensure all fields are entered and valid.')
    return render(request, "home.html", {'projects': projects})

def experience_view(request):
    experiences = Experience.objects.all()
    education_list = Education.objects.all()
    return render(request, 'experience.html', {'experiences': experiences, 'education_list': education_list})

def projectlist(request):
    # Fetch all projects and prefetch related images
    projects = list(Project.objects.prefetch_related('images').all())
    # Shuffle the list of projects randomly
    random.shuffle(projects)
    # Fetch all tags (if needed)
    tags = Tag.objects.all()
    # Pass shuffled projects and tags to the template
    return render(request, 'projectlist.html', {'projects': projects, 'tags': tags})

def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {'project': project})
