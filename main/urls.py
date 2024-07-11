from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index/", views.index, name="index"),
    path('experience/', views.experience_view, name='experience'),
    path('projectlist/', views.projectlist, name='projectlist'),
    path("project/<int:id>/", views.project, name="project"),
]