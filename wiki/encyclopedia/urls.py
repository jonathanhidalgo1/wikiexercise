from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("css", views.css, name="css"),
    path("django", views.django, name="Django"),
    path("git", views.git, name="Git"),
    path("html", views.html, name="HTML"),
    path("python", views.python, name="Python"),
    # path("<str:name>", views.pagenotfound, name="pagenotfound"),
    path("search", views.search, name="search")
    
    
]
