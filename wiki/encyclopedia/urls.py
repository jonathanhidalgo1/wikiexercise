from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),    
    path("library/<str:name>", views.library, name="library"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("library/<str:name>/edit", views.edit, name="edit"),
    path("random", views.random_page, name="random")
    
    
]
