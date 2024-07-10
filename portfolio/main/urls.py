from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path('experience/', views.experience_view, name='experience'),
    path('projectlist/', views.projectlist, name='projectlist'),
    path("project/<int:id>/", views.project, name="project"),
]